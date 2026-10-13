import streamlit as st
import pickle
import pandas as pd
from pathlib import Path

# Load the trained machine-learning model
MODEL_PATH = Path(__file__).parent / "academic_advisor_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Personal Academic Advisor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Personal Academic Advisor")
st.write("Your personal assistant for better academic performance.")

st.divider()

# Student Information
st.header("👤 Student Information")

name = st.text_input("Enter your name")

level = st.selectbox(
    "Select your level",
    ["100 Level", "200 Level", "300 Level", "400 Level", "500 Level"]
)

department = st.text_input(
    "Department",
    value="Computer Science"
)

# Academic Information
st.header("📚 Academic Information")

cgpa = st.number_input(
    "Current CGPA",
    min_value=0.0,
    max_value=5.0,
    value=3.0,
    step=0.1
)

study_hours = st.slider(
    "Daily study hours",
    0, 12, 2
)

attendance = st.slider(
    "Class attendance (%)",
    0, 100, 75
)

difficulty = st.selectbox(
    "How difficult are your courses?",
    ["Easy", "Moderate", "Difficult"]
)

# Generate Advice
if st.button("Generate My Academic Advice"):

    st.header("🎯 Your Academic Recommendations")

    if name.strip():
        st.write(f"Hello, {name}! Here is your academic advice.")
    else:
        st.write("Here are your academic recommendations.")

    st.write(f"**Level:** {level}")
    st.write(f"**Department:** {department}")

    # Use the trained machine-learning model
    student_data = pd.DataFrame(
        [[cgpa, study_hours, attendance]],
        columns=["cgpa", "study_hours", "attendance"]
    )

    prediction = model.predict(student_data)[0]

    st.subheader("🤖 AI/ML Academic Assessment")

    if prediction == "Good":
        st.success(f"Predicted support category: {prediction}")
        st.write(
            "Continue maintaining good study habits, "
            "attend classes regularly, and revise consistently."
        )

    elif prediction == "Average":
        st.info(f"Predicted support category: {prediction}")
        st.write(
            "Consider increasing your focused study time "
            "and reviewing topics you find difficult."
        )

    else:
        st.warning(f"Predicted support category: {prediction}")
        st.write(
            "You may benefit from additional academic support. "
            "Consider seeking help from lecturers, classmates, "
            "or an academic adviser."
        )

    # Additional study recommendations
    st.subheader("📖 Study Recommendations")

    if study_hours < 2:
        st.write(
            "Try building a consistent routine with "
            "2–3 focused study hours daily."
        )
    else:
        st.write(
            "Maintain your study routine and take regular breaks."
        )

    if attendance < 75:
        st.write("Attend classes more consistently.")
    else:
        st.write("Keep attending your classes regularly.")

    if difficulty == "Difficult":
        st.write(
            "Break difficult topics into smaller sections "
            "and ask lecturers or classmates for help."
        )

    st.divider()

    # Weekly Study Plan
    st.subheader("🗓️ Suggested Weekly Study Plan")

    timetable = {
        "Monday": "Review lecture notes",
        "Tuesday": "Practise programming and solve problems",
        "Wednesday": "Study difficult courses",
        "Thursday": "Complete assignments",
        "Friday": "Revise topics covered during the week",
        "Saturday": "Practise past questions",
        "Sunday": "Review progress and plan for next week"
    }

    for day, activity in timetable.items():
        st.write(f"**{day}:** {activity}")

    st.success(
        "Your recommendations are ready! "
        "Stay consistent and keep working towards your goals."
    )

    st.caption(
        "Note: This is an educational prototype. "
        "Its predictions depend on the training data and "
        "should not replace professional academic guidance."
    )