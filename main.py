#  main.py - streamlit main file
from dotenv import load_dotenv

import ui.ui_weather as ui_weather
import ui.ui_utils as ui_utils

# reads the .env file
load_dotenv()

#load html style
ui_utils.load_css("assets/styles.css")

ui_weather.show_weather_country_city_select_box()



