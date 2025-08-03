import requests, zipfile, io
import os
import pandas as pd


def get_data_weather_by_city(city: str, units="metric"):
    """
    :param city: city name
    :param units: units can be metric/imperial
    this function get a city from user
    and make an api call to openweathermap for getting weather in the entered city
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