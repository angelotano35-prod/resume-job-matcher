# Resume-Job Matcher & Cover Letter Generator

A local, offline tool that scores how well your resume matches a job description
using TF-IDF and cosine similarity (no external AI API required), then generates
a tailored cover letter draft.

## How it works
1. Paste your resume text into `data/resume.txt`
2. Paste a job posting into `data/job_description.txt`
3. Run the tool - it calculates a match score, shows matched/missing keywords,
   and generates a cover letter draft

## Tech Stack
Python, scikit-learn (TF-IDF + cosine similarity)

## Running Locally
```bash
pip install -r requirements.txt
python main.py
```

## Why TF-IDF instead of a paid AI API
TF-IDF (Term Frequency-Inverse Document Frequency) weighs words by how important
and distinctive they are across documents, and cosine similarity measures how
close two documents are in meaning based on shared important terms. This is a
real, established NLP technique - many real-world applicant tracking systems (ATS)
use similar keyword-matching approaches under the hood.
