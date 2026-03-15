import streamlit as st
from resume_parser import extract_text
from skill_matcher import match_skills

st.title("AI Resume Analyzer")

resume_file = st.file_uploader("Upload Resume", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if resume_file is not None:
        resume_text = extract_text(resume_file)
        score, matched, missing = match_skills(resume_text, job_description)

        st.subheader("Match Score")
        st.write(f"{score}%")

        st.subheader("Matched Skills")
        st.write(matched)

        st.subheader("Missing Skills")
        st.write(missing)