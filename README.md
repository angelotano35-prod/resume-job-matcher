# Resume-Job Matcher & Cover Letter Generator

An interactive dashboard that scores how well your resume matches a job description
using TF-IDF and cosine similarity (no external AI API required), then generates
a tailored cover letter draft.

## How it works

1. Run the dashboard with `streamlit run app.py`
2. Upload your resume as a PDF directly in the browser
3. Paste the job posting text into the text box
4. Fill in the job title, company name, and your name
5. Click "Analyze & Generate" to see your match score, matched/missing keywords, and a generated cover letter draft

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
