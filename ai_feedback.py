import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def generate_ai_feedback(resume_text, job_description, match_result):
    """Ask an AI model for focused, practical resume feedback."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    prompt = f"""
Review this resume against the job description.

Resume:
{resume_text[:12000]}

Job description:
{job_description[:12000]}

Keyword analysis:
Match score: {match_result['match_score']}%
Matched keywords: {', '.join(match_result['matched_keywords'])}
Missing keywords: {', '.join(match_result['missing_keywords'])}

Return concise feedback with exactly these sections:
1. Overall assessment
2. Strengths
3. Missing or weak areas
4. Three specific improvements
Do not invent experience that is not present in the resume.
"""

    response = client.responses.create(
        model=model,
        instructions="You are a careful career coach. Give honest, practical feedback.",
        input=prompt,
    )
    return response.output_text
