import streamlit as st
st.title("Student Information System")
st.header("Enter Student Details")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)
course = st.selectbox(
    "Select your course",
    ["CSE", "ECE", "EEE", "MECH", "CIVIL"]
)
if st.button("Submit"):
    st.success("Student details submitted successfully!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)