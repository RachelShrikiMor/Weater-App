import streamlit as st

def load_css(file_path: str):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def show_top_bar():
    st.markdown("""
        <div class="top-bar">
            🌍 Weather App — Powered by Streamlit
        </div>
        <div class="top-bar-spacer"></div>
    """, unsafe_allow_html=True)