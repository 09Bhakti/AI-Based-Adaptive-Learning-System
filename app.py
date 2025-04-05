import streamlit as st
from utils.recommender import recommend_content
from utils.rl_engine import train_rl_agent, recommend_difficulty
from utils.clustering import cluster_users
from utils.feedback import log_feedback

st.title("🎓 Adaptive Learning System")

user_id = st.number_input("Enter Student ID", min_value=1, step=1)
activity = st.selectbox("Choose Activity", ['lecture', 'quiz', 'assignment'])
score = st.slider("Enter Score", 0, 100)

if st.button("Recommend Content"):
    recommendation = recommend_content(user_id)
    st.write("📚 Recommended Content:", recommendation)

if st.button("Suggest Difficulty Level"):
    difficulty = recommend_difficulty(user_id, activity, score)
    st.write("🎯 Recommended Difficulty:", difficulty)

if st.button("Submit Feedback"):
    log_feedback(user_id, activity, score)
    st.success("✅ Feedback submitted successfully!")
