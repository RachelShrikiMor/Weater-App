#  main.py - streamlit main file
from dotenv import load_dotenv
import streamlit as st

import ui.ui_weather as ui_weather
import ui.ui_utils as ui_utils
import ui.ui_settings as ui_settings
import utils.settings_manager_utils as settings_manager

# reads the .env file
load_dotenv()

#load html style
ui_utils.load_css("assets/styles.css")

ui_settings.show_settings_default_location()

ui_weather.show_weather_country_city_select_box()

ui_settings.load_settings_from_file_or_session()

ui_settings.show_settings_panel_title()

ui_settings.show_settings_panel_content()







