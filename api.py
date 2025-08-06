import requests, zipfile, io
import os
import pandas as pd



def get_data_weather_by_city(city: str, units="metric"):
    """
    this function get a city from user
    and make an api call to openweathermap for getting weather in the entered city
    :param city: city name
    :param units: units can be metric/imperial
    """
    #city = input("Please enter a city: ")
    APPID = os.getenv("OPENWEATHERMAP_API_KEY")
    if city and APPID:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}&units={units}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # This parses the JSON into a Python object (usually list or dict)
            #print(data)
            #print(data["coord"]["lon"])
            #print(data["coord"]["lat"])
            return data
        else:
            #print("Failed to retrieve data:", response.status_code)
            return None
    return None

def get_cities_data_from_file_by_country_name(country_name: str):
    """
    this function returns list of all cities associated with a country
    :param country_name: country name
    """
    folder_name = "Data"
    file_name = "worldcities.csv"
    file_path = os.path.join(folder_name, file_name)

    # Check if file already exists; if so, just load it
    if os.path.exists(file_path):
        try:
             df = pd.read_csv(file_path)
             return df[df.country.str.strip().str.lower() == country_name.strip().lower()]
        except Exception as e:
            print(f"Error reading existing CSV: {e}")


    # Download and extract the ZIP file
    url = "https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error downloading file: {e}")
        return None


    #Ensure 'data' folder exists
    os.makedirs(folder_name, exist_ok=True)

    # Unzip abd Extract the csv file and save it in data folder with name worldcities.csv
    # the file will overwrite if it already exist in folder
    try:
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extract(file_name, folder_name)
    except Exception as e:
        print(f"Error extracting zip file: {e}")
        return None

    # Load and return dataframe
    try:
        df = pd.read_csv(file_path)
        return df[df.country.str.strip().str.lower() == country_name.strip().lower()]
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def get_historical_weather(lat, lon, start_date, end_date, temperature_unit):
    """
    this function get historical data for specific location and time
    this function use open-meteo api (free to use. no api-key needed)
    :param lat: latitude
    :param lon: longitude
    :param start_date: start date
    :param end_date: end date
    :param temperature_unit: celsius or fahrenheit
    :return: json
    example:
    for this call - get_historical_weather("31.4117", "35.0818", "2024-01-01", "2024-01-02", None)
    the result is for 2 days:
    {'latitude': 31.3884,
    'longitude': 35.11933,
    'generationtime_ms': 0.05340576171875,
    'utc_offset_seconds': 10800, 'timezone': 'Asia/Jerusalem',
    'timezone_abbreviation': 'GMT+3', 'elevation': 693.0,
    'daily_units': {'time': 'iso8601', 'temperature_2m_max': '°C', 'temperature_2m_min': '°C'},
    'daily': {
    'time': ['2024-01-01', '2024-01-02'],
    'temperature_2m_max': [16.3, 14.9], 'temperature_2m_min': [10.1, 8.8]
    } }
    """
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min", #for show the max\min daily temperature
        "timezone": "auto", #time zone by coordinates
        "temperature_unit": temperature_unit
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error getting historical weather data: {e}")
        return None


