import streamlit as st
from pdfminer.high_level import extract_text
import tempfile
import spacy

nlp = spacy.load("en_core_web_sm")
skills_db = [
    "java", "spring boot", "microservices", "restful apis",
    "sql", "nosql", "hibernate", "jpa",
    "maven", "gradle", "git", "docker",
    "kubernetes", "aws", "azure", "gcp",
    "redis", "kafka", "react", "github"
]

def clean_text(text):
    doc = nlp(text)
    words = []

    for token in doc:
        if not token.is_stop and token.is_alpha:
            if token.text.lower() in ["aws", "sql", "ai"]:
                words.append(token.text.lower())
            else:
                words.append(token.lemma_.lower())

    return words

def extract_skills(words):
    found_skills = []
    text = " ".join(words).lower()
    word_set = set(words)

    for skill in skills_db:
        if " " in skill:
            if skill in text:
                found_skills.append(skill)
        else:
            if skill in word_set:
                found_skills.append(skill)

    return found_skills

st.title("Resume Analzer")
name = st.text_input("Enter your name")
jd = st.text_area("Enter the job description")
resume = st.file_uploader("Upload Resume(Pdf/txt)",type=["pdf","txt"])

def read_resume(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            return extract_text(tmp.name)

    else:
        return ""
    
def match_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0, set()

    matched = set(resume_skills) & set(job_skills)
    score = len(matched) / len(job_skills) * 100

    return score, matched
    
if st.button("Analyze Resume"):
    if resume is not None and jd.strip() != "":

        resume_text = read_resume(resume)
        resume_words = clean_text(resume_text)
        resume_skills = extract_skills(resume_words)

        job_words = clean_text(jd)
        job_skills = extract_skills(job_words)

        score, matched = match_score(resume_skills, job_skills)
        missing = set(job_skills) - set(resume_skills)

    
        st.subheader(f"Hello {name} ")

        st.write("###  Match Score:")
        st.success(f"{score:.2f}%")

        st.write("###  Matched Skills:")
        if matched:
            st.write(list(matched))
        else:
            st.warning("No matching skills found")

        st.write("###  Missing Skills:")
        if missing:
            st.write(list(missing))
        else:
            st.success("No missing skills found")

    else:
        st.error("Please upload resume and enter job description")