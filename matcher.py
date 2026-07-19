from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# A curated list of real IT/tech/QA skill terms to match against.
# This avoids picking up generic resume boilerplate (e.g. "graduated", "city", "use")
# that plain TF-IDF top-words would otherwise surface on short documents.
SKILL_KEYWORDS = [
    # Languages
    "python", "java", "javascript", "c#", "c++", "sql", "html", "css", "dart", "typescript",
    # QA / testing
    "qa", "quality assurance", "testing", "test automation", "selenium", "playwright",
    "cypress", "manual testing", "regression testing", "test cases", "bug tracking",
    "jira", "test plans", "unit testing", "integration testing", "api testing",
    # Dev tools / frameworks
    "flutter", "react", "node", "flask", "django", "spring boot", "git", "github",
    "unity", "android studio", "firebase", "rest api", "postman",
    # Data
    "data analysis", "excel", "power bi", "tableau", "pandas", "data visualization",
    "database", "sqlite", "mysql", "postgresql",
    # IT support / networking
    "networking", "troubleshooting", "linux", "unix", "windows server", "cybersecurity",
    "packet tracer", "service desk", "technical support", "help desk", "it support",
    "system administration", "cloud", "aws", "azure",
    # Soft skills (still worth flagging if job posting emphasizes them)
    "communication", "problem-solving", "problem solving", "teamwork", "collaboration",
    "leadership", "attention to detail", "adaptability", "time management",
    # Office / design
    "powerpoint", "microsoft office", "word", "figma", "photoshop", "premiere",
]

# Words that show up frequently in resumes/job posts but aren't meaningful skills
EXTRA_STOPWORDS = {
    "graduated", "city", "address", "email", "cellular", "experience", "skills",
    "work", "use", "used", "using", "results", "driven", "seeking", "position",
    "apply", "team", "entry", "level", "role", "job", "years", "strong", "proficient",
    "background", "responsibilities", "duties", "requirements", "candidate", "company",
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s#+.]", " ", text)
    return text


def get_match_score(resume_text, job_text):
    """Returns a 0-100 similarity score between resume and job description."""
    documents = [clean_text(resume_text), clean_text(job_text)]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 1)


def find_skills_in_text(text):
    """Finds which curated skill keywords actually appear in the given text."""
    cleaned = clean_text(text)
    found = []
    for skill in SKILL_KEYWORDS:
        if skill in cleaned:
            found.append(skill)
    return found


def get_top_keywords(text, top_n=10):
    """
    Returns the most relevant skill keywords found in the text.
    Prefers curated skill matches; falls back to TF-IDF filtered
    against EXTRA_STOPWORDS if too few curated skills are found.
    """
    found_skills = find_skills_in_text(text)
    if len(found_skills) >= 5:
        return found_skills[:top_n]

    # Fallback: TF-IDF, but filter out boilerplate words
    vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n * 3)
    vectorizer.fit([clean_text(text)])
    candidates = vectorizer.get_feature_names_out()
    filtered = [w for w in candidates if w not in EXTRA_STOPWORDS and len(w) > 2]
    combined = found_skills + filtered
    # de-duplicate while preserving order
    seen = set()
    result = []
    for w in combined:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result[:top_n]


def get_missing_keywords(resume_text, job_text, top_n=15):
    """Finds important job-description skills that are missing from the resume."""
    job_skills = set(get_top_keywords(job_text, top_n=top_n))
    resume_skills = set(get_top_keywords(resume_text, top_n=top_n))

    # Also check curated list membership directly for better accuracy
    job_curated = set(find_skills_in_text(job_text))
    resume_curated = set(find_skills_in_text(resume_text))

    all_job_skills = job_skills | job_curated
    all_resume_skills = resume_skills | resume_curated

    matched = sorted(all_job_skills & all_resume_skills)
    missing = sorted(all_job_skills - all_resume_skills)
    return matched, missing