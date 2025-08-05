import streamlit as st

def load_css(file_path: str):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def show_top_bar():
    st.header("🌍 Weather App — Powered by Streamlit", divider="orange", width="stretch")
    #st.write("🌍 Weather App — Powered by Streamlit")
    #st.markdown("""
    #    <div class="top-bar">
    #        🌍 Weather App — Powered by Streamlit
    #    </div>
    #    <div class="top-bar-spacer"></div>
    #""", unsafe_allow_html=True)

def show_feedback():
    st.write(":orange[**rate us**]")
    selected = st.feedback("stars")
    if selected:
        st.write("Thanks for your feedback")

def show_rights_reserved():
    st.write("© All rights reserved to Shriki Rachel")