import streamlit as st
st.title("HomeAid AI™")
st.caption("© Ryan Edward Brown | Nov 2, 2025")

query = st.text_input("Client needs (e.g., housing + mental health in LA):")
if st.button("Find Resources"):
    with st.spinner("Matching..."):
        st.success("Top 3 Matches:")
        st.write("1. Emergency Shelter (211 CA)")
        st.write("2. EDD Job Portal")
        st.write("3. CalFresh Pre-Screener")
