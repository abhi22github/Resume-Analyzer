#  Resume Analyzer & Job Matcher

An intelligent Python tool that leverages Natural Language Processing (NLP) to bridge the gap between job seekers and recruitment requirements. This tool parses resumes, extracts technical skills, and provides a quantitative match score against specific job descriptions.

---

## Key Features

* **Multi-format Support:** Handles both `.pdf` (via `pdfminer`) and `.txt` files.
* **NLP Text Processing:** Uses spaCy for tokenization and lemmatization to ensure "Developing" and "Developer" are treated as the same skill.
* **Smart Skill Extraction:** Utilizes a specialized dictionary to identify technical competencies while protecting industry acronyms (e.g., AWS, SQL).
* **Gap Analysis:** Instantly identifies "Missing Skills" to help candidates tailor their resumes.
* **Match Scoring:** Calculates a percentage-based score to evaluate candidate suitability.
* **Interactive UI:** Built using Streamlit for real-time analysis and user-friendly interaction.

---

##  Tech Stack

* **Language:** Python 3.x
* **Frontend + Backend:** Streamlit
* **NLP Library:** spaCy (`en_core_web_sm`)
* **PDF Parser:** pdfminer

---

## Project Flow

* Upload your resume
* NLP analyses it
* Checks for matching skills along with job description
* Provides the final score and missing skills 

---

