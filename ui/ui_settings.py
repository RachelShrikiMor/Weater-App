import streamlit as st

import  utils.settings_manager_utils as settings_manager
import  api as api

def show_settings_panel_title():
    """ this function draw title on settings sidebar """
    st.sidebar.title("⚙️ Settings")

def load_settings_from_file_or_session():
    """
    this function Load settings at start website entry
    from settings.json file or from session
    """
    if "settings" not in st.session_state:
        st.session_state.settings = settings_manager.load_settings()
    user_settings = st.session_state.settings

    # Initialize units from settings only if not already set
    if "units" not in st.session_state:
        st.session_state.units = user_settings.get("units", "metric")
        st.session_state.units_sign = "C" if st.session_state.units == "metric" else "F"

def show_settings_panel_content():
    """
    this function create a form inside the sidebar
    when press the button to submit, settings saved in settings.json file
    """

    # Read current unit setting from session
    current_units = st.session_state.get("units", "metric")

    with st.sidebar.form("settings_form"):
        selected_units = st.radio("Units", ["metric", "imperial"], index=0 if current_units == "metric" else 1)
        submitted = st.form_submit_button("Save Settings")

        # Show current settings
        if submitted:
            st.success(f"Settings saved! to {selected_units}", icon="✅")
            # using session
            st.session_state.units = selected_units
            st.session_state.units_sign = "C" if selected_units == "metric" else "F"
            # st.session_state.lang = selected_lang
            # st.session_state.dark = dark_mode
            settings_manager.set_units(selected_units)  # save the units into settings.json file
            # 🔁 Force Streamlit to rerun and reflect the new settings
            st.rerun()

def show_settings_default_location():
    # Use current units from session
    user_default_location = settings_manager.get_default_location() #user_default_location: dict[str, str]
    units = st.session_state.get("units", "metric")
    units_sign = st.session_state.get("units_sign", "C")

    if user_default_location and "country" in user_default_location and "city" in user_default_location:
        user_default_country = user_default_location['country']
        user_default_city = user_default_location['city']
        if user_default_country and user_default_city:
            st.text(f"your default location is: {user_default_city} ,{user_default_country}")
            data_default_location = api.get_data_weather_by_city(user_default_city, units)
            if data_default_location:
                st.text(f"{data_default_location['main']['temp']} {units_sign}°")
                st.write(f"↓{data_default_location['main']['temp_min']} / {data_default_location['main']['temp_max']}↑")

def show_button_save_default_location(country, city):
    """
    this function create and display button to save default user location
    :param country: country name
    :param city: city name
    """
    if st.button(f"Set {city},{country} as default location", icon="🌍"):
        settings_manager.set_default_location(country, city)
        st.success(f"Set default location to {city}, {country}")
        st.rerun()


