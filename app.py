import streamlit as st

# Page setup
st.set_page_config(page_title="Resume & Cover Letter Helper", page_icon="📄", layout="centered")

st.title("📄 Resume & Cover Letter Helper")
st.write("Generate professional resume summaries and customized cover letters instantly!")

# Tabs for separate features
tab1, tab2 = st.tabs(["📝 Resume Summary Helper", "✉️ Cover Letter Generator"])

# --- TAB 1: RESUME SUMMARY ---
with tab1:
    st.header("Resume Summary Builder")
    job_title = st.text_input("Job Title / Target Role:", placeholder="e.g. Data Analyst, Software Engineer")
    years_exp = st.number_input("Years of Experience:", min_value=0, max_value=40, value=1)
    key_skills = st.text_input("Key Skills (comma separated):", placeholder="e.g. Python, SQL, Machine Learning")
    
    if st.button("Generate Resume Summary"):
        if job_title and key_skills:
            st.success("🎉 Resume Summary Generated!")
            summary = (
                f"Motivated and detail-oriented {job_title} with {years_exp}+ year(s) of practical experience. "
                f"Proficient in {key_skills}. Adept at problem-solving, collaboration, and delivering scalable solutions "
                f"in fast-paced environments."
            )
            st.text_area("Copy your Summary:", value=summary, height=120)
        else:
            st.warning("⚠️ Please fill in both Job Title and Key Skills!")

# --- TAB 2: COVER LETTER ---
with tab2:
    st.header("Cover Letter Generator")
    full_name = st.text_input("Your Full Name:", placeholder="e.g. John Doe")
    company_name = st.text_input("Company Name:", placeholder="e.g. TechCorp")
    role_applied = st.text_input("Role You Are Applying For:", placeholder="e.g. AI Engineer Intern")
    candidate_skills = st.text_area("Your Core Strengths & Skills:", placeholder="e.g. Python programming, data analysis, deep learning, git")
    
    if st.button("Generate Cover Letter"):
        if full_name and company_name and role_applied:
            st.success("🎉 Cover Letter Generated!")
            cover_letter = f"""Dear Hiring Manager at {company_name},

I am writing to express my strong interest in the {role_applied} position at {company_name}. With my solid foundation in technical concepts and hands-on project experience, I am confident in my ability to contribute effectively to your team.

My technical background includes experience with {candidate_skills}. I thrive in collaborative environments and am passionate about applying my skills to solve real-world problems and drive impactful outcomes.

I am eager to bring my background, dedication, and problem-solving skills to {company_name}. Thank you for your time and consideration.

Sincerely,
{full_name}"""
            st.text_area("Copy your Cover Letter:", value=cover_letter, height=300)
        else:
            st.warning("⚠️ Please fill in Full Name, Company Name, and Role Applied!")
