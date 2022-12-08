import streamlit as st

st.set_page_config(page_title="Elie Levy's Portfolio", page_icon="👋",)
st.write("# Welcome to Elie Levy's Portfolio ! 👋")
st.sidebar.success("Select a project above.")

st.markdown(
    """
    As a Data Engineer, please find in this portfolio some projects I have worked on.
    **👉 Select a demo from the sidebar** to see some examples
    ### Wondering what's on the menu ? 
    - AirBnb Exploration 🏠 : Discover the available homes in the London Area
    - Uber Exploration 🚕 : Visualize Uber pickupds in NYC
    - Cloud Certification Quizz 📚 : Get some training to ace your GCP Certification
    - MoneyBall Reloaded 🏀 : Analyze NBA Data to find the perfect player
    ### Want to check the code ? 
    - [Help yourself](https://github.com/elielevy3/PORTFOLIO)
"""
)