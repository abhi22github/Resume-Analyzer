# Resume Analyzer & Job Matcher 

An intelligent Python tool that leverages Natural Language Processing (NLP) to bridge the gap between job seekers and recruitment requirements. This tool parses resumes, extracts technical skills, and provides a quantitative match score against specific job descriptions.

##  Key Features
* **Multi-format Support:** Handles both `.pdf` (via `pdfminer`) and `.txt` files.
* **NLP Text Processing:** Uses `spaCy` for tokenization and lemmatization to ensure "Developing" and "Developer" are treated as the same skill.
* **Smart Skill Extraction:** Utilizes a specialized dictionary to identify technical competencies while protecting industry acronyms (e.g., AWS, SQL).
* **Gap Analysis:** Instantly identifies "Missing Skills" to help candidates tailor their resumes.
* **Match Scoring:** Calculates a percentage-based score to evaluate candidate suitability.

##  Tech Stack
* **Language:** Python 3.x
* **NLP Library:** [spaCy](https://spacy.io/) (`en_core_web_sm`)
* **PDF Parser:** `pdfminer.six`

## Program Flow

* Extraction: Converts raw file data into strings.
* Cleaning: Removes "stop words" and punctuation; converts words to their base (lemma) form.
* Skill Filtering: Cross-references cleaned words against a skills_db list.
* Comparison: Uses Python sets to calculate the intersection (Matches) and difference (Gaps) between the Resume and the Job Description.
