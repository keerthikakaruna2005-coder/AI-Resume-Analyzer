import streamlit as st
from PyPDF2 import PdfReader


# Title
st.title("🤖 AI Resume Analyzer")

st.write(
    "Upload your resume and get skill analysis, resume score, "
    "job recommendations and improvement suggestions."
)


# Skill Database
skills_database = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "artificial intelligence",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "streamlit",
    "github",
    "git",
    "docker",
    "aws"
]


# Job Roles
job_roles = {

    "Software Developer":
    ["python", "java", "sql", "javascript", "git"],

    "Data Analyst":
    ["python", "sql", "data analysis", "pandas", "numpy"],

    "Machine Learning Engineer":
    ["python", "machine learning", "scikit-learn", "numpy", "pandas"],

    "Web Developer":
    ["html", "css", "javascript", "git"]

}


# Suggestions
skill_suggestions = {

    "aws": "Learn AWS cloud services like EC2 and S3",

    "docker": "Learn Docker for application deployment",

    "github": "Upload more projects and improve Git skills",

    "machine learning": "Learn deep learning and model deployment",

    "sql": "Practice advanced SQL queries"

}


# Upload Resume

uploaded_file = st.file_uploader(
    "Upload your Resume PDF",
    type="pdf"
)


if uploaded_file:

    # Extract Text
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()


    resume_text = resume_text.lower()


    st.success("Resume uploaded successfully")


    # Skill Extraction

    detected_skills = []

    for skill in skills_database:

        if skill in resume_text:
            detected_skills.append(skill)


    st.subheader("✅ Detected Skills")

    if detected_skills:
        for skill in detected_skills:
            st.write("✔", skill)

    else:
        st.write("No skills detected")


    # Resume Score

    required_skills = skills_database

    score = (
        len(set(detected_skills) &
        set(required_skills))
        /
        len(required_skills)
    ) * 100


    st.subheader("📊 Resume Score")

    st.write(round(score,2), "%")


    # Missing Skills

    missing_skills = list(
        set(required_skills)
        -
        set(detected_skills)
    )


    st.subheader("❌ Missing Skills")

    for skill in missing_skills:
        st.write(skill)


    # Job Recommendation

    st.subheader("💼 Recommended Roles")


    role_scores = {}


    for role, skills in job_roles.items():

        match = len(
            set(detected_skills)
            &
            set(skills)
        )

        role_scores[role] = (
            match / len(skills)
        ) * 100


    for role, score in sorted(
        role_scores.items(),
        key=lambda x:x[1],
        reverse=True
    ):

        st.write(
            role,
            ":",
            round(score,2),
            "%"
        )


    # Suggestions

    st.subheader("🚀 AI Improvement Suggestions")


    for skill in missing_skills:

        if skill in skill_suggestions:

            st.write(
                "➡",
                skill_suggestions[skill]
            )
