import re


STOP_WORDS = {
    "the", "and", "for", "with", "that", "this", "from", "into",
    "have", "has", "will", "your", "their", "about", "using", "work",
    "role", "team", "years", "experience", "skills", "job", "resume",
    "developer", "software", "strong", "good", "excellent",
}


def normalize_text(text):
    """Convert text to lowercase and keep only letters and numbers."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


def extract_keywords(text, min_length=2):
    """Return a set of useful words from the text."""
    normalized = normalize_text(text)
    words = normalized.split()

    keywords = {
        word for word in words
        if len(word) >= min_length and word not in STOP_WORDS
    }
    return keywords


def compare_resume_to_job(resume_text, job_description):
    """Return a simple match score and missing keywords."""
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    matched = sorted(resume_keywords & job_keywords)
    missing = sorted(job_keywords - resume_keywords)

    if not job_keywords:
        return {
            "match_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "summary": "No job description keywords available."
        }

    score = round((len(matched) / len(job_keywords)) * 100)

    return {
        "match_score": score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "summary": (
            f"Your resume matches {score}% of the job description keywords. "
            f"You are missing: {', '.join(missing[:5]) if missing else 'no major gaps'}"
        )
    }


if __name__ == "__main__":
    resume = """
    Python developer with SQL, AWS, and machine learning experience.
    Built dashboards and worked with APIs and data pipelines.
    """

    job = """
    Looking for a Python developer with SQL, AWS, and data engineering experience.
    Must have strong API and ETL skills.
    """

    result = compare_resume_to_job(resume, job)
    print(result)
