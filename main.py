#  main.py - streamlit main file
from dotenv import load_dotenv

import ui.ui_weather as ui_weather
import ui.ui_utils as ui_utils
import ui.ui_settings as ui_settings
import ui.ui_favorite as ui_favorite

# reads the .env file
load_dotenv()

#load html style
ui_utils.load_css("assets/styles.css")

ui_utils.show_top_bar()

#load session settings
ui_settings.load_settings_from_file_or_session()

# show/hide favorites
ui_favorite.show_favorite_locations_table()

ui_settings.show_settings_default_location()

ui_weather.show_weather_country_city_select_box()

ui_settings.show_settings_panel_title()

ui_settings.show_settings_panel_content()







