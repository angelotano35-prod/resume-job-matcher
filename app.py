"""
Run this with: streamlit run app.py
(run it from the resume-job-matcher root folder)

Upload your resume as a PDF, paste a job description, and get a match score,
keyword analysis, and a generated cover letter draft - all in a browser dashboard.
"""

import streamlit as st
from pypdf import PdfReader
from matcher import get_match_score, get_missing_keywords, get_top_keywords
from cover_letter_generator import generate_cover_letter

st.set_page_config(page_title="Resume-Job Matcher", layout="wide")

st.title("📄 Resume-Job Matcher & Cover Letter Generator")
st.caption("Upload your resume (PDF) and paste a job description to see how well they match.")


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload your resume")
    resume_file = st.file_uploader("Upload a PDF resume", type=["pdf"])

with col2:
    st.subheader("2. Paste the job description")
    job_text = st.text_area("Paste the full job posting text here", height=250)

st.divider()

# --- Extra info for the cover letter ---
st.subheader("3. A few details for your cover letter")
c1, c2, c3 = st.columns(3)
job_title = c1.text_input("Job title")
company_name = c2.text_input("Company name")
your_name = c3.text_input("Your full name")

st.divider()

# --- Run analysis ---
if st.button("Analyze & Generate", type="primary"):
    if not resume_file:
        st.warning("Please upload your resume PDF first.")
    elif not job_text.strip():
        st.warning("Please paste a job description first.")
    else:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)

            score = get_match_score(resume_text, job_text)
            matched, missing = get_missing_keywords(resume_text, job_text)
            resume_top_skills = list(get_top_keywords(resume_text, top_n=10))

        # --- Results ---
        st.subheader("Results")

        m1, m2, m3 = st.columns(3)
        m1.metric("Match Score", f"{score}%")
        m2.metric("Matched Keywords", len(matched))
        m3.metric("Missing Keywords", len(missing))

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**✅ Matched keywords (already in your resume):**")
            st.write(", ".join(matched) if matched else "None found")
        with col_b:
            st.markdown("**⚠️ Missing keywords (in job posting, not in resume):**")
            st.write(", ".join(missing) if missing else "None missing — great coverage!")

        st.divider()

        # --- Cover letter ---
        st.subheader("Generated Cover Letter Draft")
        letter = generate_cover_letter(
            job_title=job_title or "the position",
            company_name=company_name or "your company",
            your_name=your_name or "Your Name",
            matched_keywords=matched,
            top_skills=resume_top_skills,
        )
        st.text_area("Edit before sending:", value=letter, height=300)

        st.download_button(
            "Download Cover Letter",
            data=letter,
            file_name="cover_letter.txt",
            mime="text/plain",
        )
