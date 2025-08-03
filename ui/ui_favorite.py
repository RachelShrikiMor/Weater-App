import streamlit as st
import pandas as pd

import  utils.settings_manager_utils as settings_manager

def show_favorite_locations_table():
    with st.expander("Click to expand favorites"):
        favorites = settings_manager.get_favorite_locations()
        if favorites:
            df = pd.DataFrame(favorites)
            st.table(df)
        else:
            st.info("No favorite locations saved yet.")

def show_button_add_favorite(country, city):
    if st.button(f"Add {city},{country} to favorites location", icon="⭐"):
        settings_manager.add_favorite_location(country, city)
        st.success(f"Add {city}, {country} to favorites location")
        st.rerun()  # 🔁 Force the app to re-run and reflect updated favorites