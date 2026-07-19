# Resume-Job Matcher & Cover Letter Generator

An interactive dashboard that scores how well your resume matches a job description
using TF-IDF and cosine similarity (no external AI API required), then generates
a tailored cover letter draft.

## Features
- Upload your resume directly as a PDF
- Paste any job description
- Get a match score, matched keywords, and missing keywords
- Auto-generated cover letter draft, editable and downloadable

## Tech Stack
Python, Streamlit, pypdf, scikit-learn (TF-IDF + cosine similarity)

## Running Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Why TF-IDF instead of a paid AI API
TF-IDF (Term Frequency-Inverse Document Frequency) weighs words by how important
and distinctive they are across documents, and cosine similarity measures how
close two documents are in meaning based on shared important terms. Combined with
a curated list of real IT/QA skill keywords, this gives reliable, relevant matches
without needing a paid AI API. This mirrors how many real-world applicant tracking
systems (ATS) score resumes under the hood.
