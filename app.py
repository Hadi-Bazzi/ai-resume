import streamlit as st

from ai_feedback import generate_ai_feedback
from resume_matcher import compare_resume_to_job
from resume_parser import clean_resume_text, extract_text_from_pdf


st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("AI Resume Analyzer")
st.write("Upload a resume and compare it with a job description.")

resume_file = st.file_uploader("Upload your resume as a PDF", type=["pdf"])
job_description = st.text_area(
    "Paste the job description",
    height=240,
    placeholder="Paste the responsibilities and requirements here...",
)

if st.button("Analyze resume", type="primary"):
    if resume_file is None:
        st.warning("Please upload a PDF resume first.")
    elif not job_description.strip():
        st.warning("Please paste a job description first.")
    else:
        raw_text = extract_text_from_pdf(resume_file.getvalue())
        resume_text = clean_resume_text(raw_text)
        result = compare_resume_to_job(resume_text, job_description)

        st.metric("Keyword match", f"{result['match_score']}%")
        st.write(result["summary"])

        st.subheader("Matched keywords")
        st.write(", ".join(result["matched_keywords"])
                 or "No matches found yet.")

        st.subheader("Keywords to review")
        st.write(", ".join(result["missing_keywords"])
                 or "No obvious keyword gaps.")

        st.subheader("AI feedback")
        with st.spinner("Generating personalized feedback..."):
            feedback = generate_ai_feedback(
                resume_text,
                job_description,
                result,
            )

        if feedback:
            st.markdown(feedback)
        else:
            st.info(
                "Add OPENAI_API_KEY to your .env file to enable AI feedback."
            )
