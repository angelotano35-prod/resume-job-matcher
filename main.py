from matcher import get_match_score, get_missing_keywords, get_top_keywords
from cover_letter_generator import generate_cover_letter

RESUME_PATH = "data/resume.txt"
JOB_PATH = "data/job_description.txt"
OUTPUT_PATH = "output_cover_letter.txt"


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    resume_text = load_text(RESUME_PATH)
    job_text = load_text(JOB_PATH)

    print("Analyzing resume against job description...\n")

    score = get_match_score(resume_text, job_text)
    matched, missing = get_missing_keywords(resume_text, job_text)
    resume_top_skills = list(get_top_keywords(resume_text, top_n=10))

    print(f"Match Score: {score}%\n")
    print("Matched keywords (already in your resume):")
    print(", ".join(matched) if matched else "None found")
    print()
    print("Missing keywords (in job posting, not in your resume):")
    print(", ".join(missing) if missing else "None missing - great coverage!")
    print()

    job_title = input("Enter the job title you are applying for: ")
    company_name = input("Enter the company name: ")
    your_name = input("Enter your full name: ")

    letter = generate_cover_letter(
        job_title=job_title,
        company_name=company_name,
        your_name=your_name,
        matched_keywords=matched,
        top_skills=resume_top_skills,
    )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(letter)

    print(f"\nCover letter draft saved to {OUTPUT_PATH}")
    print("Remember to review and personalize it further before sending.")


if __name__ == "__main__":
    main()
