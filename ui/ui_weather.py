import streamlit as st
import pycountry

import api as api
import utils.timezone_utils as timezone_utils
import ui.ui_settings as ui_settings
import ui.ui_favorite as ui_favorite
import ui.ui_map as ui_map


def show_weather_country_city_select_box():
    """
        this function load the countries
        and cities by the choosing country
        and show country select_box and city select_box for user
    """
    countries = get_countries_dic()
    # sorted(countries.keys())
    selected_country = st.selectbox("Please select a country", sorted(countries.keys()), index=None,
                                    placeholder="Please select a country")

    if selected_country:
        st.text(selected_country)
        df_cities = api.get_cities_data_from_file_by_country_name(selected_country)
        if df_cities is not None and not df_cities.empty:
            cities = df_cities.city

            # city names based on country, show relevant dropdown cities
            selected_city = st.selectbox("Please select a city", cities, index=None,
                                         placeholder="Please select city from the list")
            if selected_city:

                city_data = df_cities[df_cities.city.str.strip().str.lower() == selected_city.strip().lower()]
                st.text(selected_city)

                lat = city_data.lat.iloc[0]
                lng = city_data.lng.iloc[0]

                show_curr_time_location(selected_city, selected_country, lng, lat)

                ui_settings.show_button_save_default_location(selected_country, selected_city)

                ui_favorite.show_button_add_favorite(selected_country, selected_city)

                data = api.get_data_weather_by_city(selected_city, units=st.session_state.units)
                if data:
                    show_weather_details(data, selected_city, selected_country,  st.session_state.units_sign)
                    ui_map.show_map_for_location(lat, lng, selected_city, selected_country)
        else:
            st.error("City not found in data.")


def show_weather_details(data, city, country, units_sign):
    """
    this function show the weather data to user
    :param data: data from api
    :param city: city selected by user
    :param country: country selected by user
    :param units_sign: C or F
    """
    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    sea_level = data["main"]["sea_level"]

    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    visibility = data["visibility"]

    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]

    title = f"Weather in {city}, {country}"
    st.title(f"{title}")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.title(f"{temp} {units_sign}°")
    with col2:
        st.image(f"https://openweathermap.org/img/wn/{icon}@2x.png", width=60)

    st.write(f"{description}")
    st.write(f"↓{temp_min} / {temp_max}↑")
    st.write(f"feels like {feels_like} {units_sign}°")

    col1, col2, col3 = st.columns(3)
    col1.metric("pressure", value=pressure)
    col2.metric("humidity", value=humidity)
    col3.metric("sea level", value=sea_level)

def get_countries_dic():
    """this function gets all countries as dictionary
     use for user choose"""
    lst_countries = list(pycountry.countries)
    countries_dic = {country.name: country.alpha_2 for country in lst_countries}
    return countries_dic

def show_curr_time_location(city: str, country: str, lng, lat):
    """
    this function show current date and time
    according location data:longitude, latitude
    :param city: city name
    :param country: country name
    :param lng: longitude location
    :param lat: latitude location
    """
    formatted_user_time = timezone_utils.display_date_time(lng, lat)
    st.write(f"current date and time in {city}, {country} is: {formatted_user_time}")






