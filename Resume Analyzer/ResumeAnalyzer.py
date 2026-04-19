import spacy
from pdfminer.high_level import extract_text


nlp = spacy.load("en_core_web_sm")

file_path = str(input("Enter file name(txt/pdf):"))

def read_resume(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    
    elif file_path.endswith(".pdf"):
        return extract_text(file_path)
    
    else:
        print("Unsupported file format")
        return ""

  

content = read_resume(file_path)

doc = nlp(content)

cleaned_words = []

for token in doc:
    if not token.is_stop and token.is_alpha:
        if token.text.lower() in ["aws", "sql", "ai"]:
            cleaned_words.append(token.text.lower())
        else:
            cleaned_words.append(token.lemma_.lower())   



skills_db = [
    "java", "spring boot", "microservices", "restful apis",
    "sql", "nosql", "hibernate", "jpa",
    "maven", "gradle", "git", "docker",
    "kubernetes", "aws", "azure", "gcp",
    "redis", "kafka", "react", "github"
]

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

resume_skills = extract_skills(cleaned_words)


job_desc = """
We are looking for a Backend Developer with strong experience in Java and Spring Boot.
The candidate should be able to design and develop RESTful APIs and work with databases.

Required Skills:
- Java
- Spring Boot
- RESTful APIs
- SQL
- AWS
- Git
- Docker

Responsibilities:
- Develop scalable backend services
- Integrate APIs with frontend applications
- Work with cloud platforms like AWS
"""

job_doc = nlp(job_desc)

job_words = []

for token in job_doc:
    if not token.is_stop and token.is_alpha:
        if token.text.lower() in ["aws", "sql", "ai"]:
            job_words.append(token.text.lower())
        else:
            job_words.append(token.lemma_.lower())




job_skills = extract_skills(job_words)
print("Job Skills:", job_skills)


def match_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0, set()

    matched = set(resume_skills) & set(job_skills)
    score = len(matched) / len(job_skills) * 100

    return score, matched

score, matched = match_score(resume_skills, job_skills)

print("Match Score:", score)
if matched:
    print("Matched Skills:", matched)
else:
    print("Matched Skills: No Matches.This role is not suitable for you")

missing_skills = set(job_skills) - set(resume_skills)

if missing_skills:
    print("Missing Skills:", missing_skills)
else:
    print("Missing Skills: None")
