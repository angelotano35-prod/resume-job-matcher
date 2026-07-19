COVER_LETTER_TEMPLATE = """Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company_name}. With a background in {top_skills}, I am confident I can contribute meaningfully to your team.

In my recent experience, I have developed strong skills in {matched_keywords}, which align closely with what you are looking for in this role. I am particularly drawn to this opportunity because it allows me to apply my technical background while continuing to grow as a professional.

I would welcome the chance to discuss how my skills and experience can support {company_name}'s goals. Thank you for considering my application.

Sincerely,
{your_name}
"""


def generate_cover_letter(job_title, company_name, your_name, matched_keywords, top_skills):
    matched_str = ", ".join(matched_keywords[:6]) if matched_keywords else "relevant technical skills"
    skills_str = ", ".join(top_skills[:3]) if top_skills else "software development and IT"

    return COVER_LETTER_TEMPLATE.format(
        job_title=job_title,
        company_name=company_name,
        your_name=your_name,
        matched_keywords=matched_str,
        top_skills=skills_str,
    )
