
import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills, calculate_match_score
from semantic_matcher import calculate_semantic_similarity
import plotly.express as px

# Load skills list
with open("skills_list.txt", "r") as f:
    all_skills = [line.strip() for line in f.readlines() if line.strip() != ""]

st.set_page_config(page_title="AI Resume Screening", layout="centered")
st.title("📄 AI Resume Screening App")

# File uploader for resume
resume_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

# Text area for job description
job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze Resume"):
    if resume_file is not None and job_description.strip() != "":
        # Extract resume text
        resume_text = extract_text_from_pdf(resume_file)

        # Extract skills from resume and job description
        resume_skills = extract_skills(resume_text, all_skills)
        jd_skills = extract_skills(job_description, all_skills)

        # Calculate skill-based match score
        score, matched, missing = calculate_match_score(resume_skills, jd_skills)

        # 🧠 Calculate semantic similarity score
        semantic_score = calculate_semantic_similarity(resume_text, job_description)

        # 🤝 Combine both scores into a hybrid score
        combined_score = int((score * 0.4) + (semantic_score * 0.6))


        # Display results
        st.success(f"✅ Skill Match Score: {score}%")
        st.info(f"🧠 Semantic Similarity Score: {semantic_score}%")
        st.markdown(f"### 🤝 Combined Relevance Score: **{combined_score}%**")
        st.markdown(f"**🎯 Matched Skills:** {', '.join(matched) if matched else 'None'}")
        # st.markdown(f"**🚫 Missing Skills:** {', '.join(missing) if missing else 'None'}")
        # 🔍 Neat missing skills display
        if missing:
            st.warning("🔍 **You can improve your resume by adding these skills:**")
            for skill in sorted(missing):
                st.markdown(f"- {skill}")
        else:
            st.success("🎉 Awesome! Your resume covers all required skills.")

         # Display pie chart
        chart_data = {
            'Category': ['Matched Skills', 'Missing Skills'],
            'Count': [len(matched), len(missing)]
        }
        fig = px.pie(chart_data, names='Category', values='Count', title='Skill Match Breakdown')
        st.plotly_chart(fig)    


       

    else:
        st.warning("⚠️ Please upload a resume and paste the job description.")
