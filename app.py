import streamlit as st
from src.experiment import run_experiment

st.set_page_config(
    page_title="AI Decision Impact Platform",
    layout="centered"
)

st.title("AI Decision Experimentation & Impact Platform")
st.write("Compare decision policies using business impact metrics")

if st.button("Run Experiment"):
    results = run_experiment()

    st.subheader("Policy Comparison")
    st.dataframe(results["summary_table"])

    st.subheader("Recommended Policy")
    st.success(results["recommended_policy"])
