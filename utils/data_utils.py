import api as api
#import  streamlit as st

from typing import Any
from datetime import datetime

def get_yearly_weather(lat, lon, year, units):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    return api.get_historical_weather(lat, lon, start_date, end_date, units)

def get_average_yearly_weather(data: dict[str, Any]):
    if data:
        temps = data.get("daily", {}).get("temperature_2m_max", [])
        if temps:
            return sum(temps) / len(temps)  # Average max temperature
    return None

def get_average_data_for_past_years(lat, lon, units, num_years):
    temperature_unit = "celsius"
    if units == "imperial": temperature_unit="fahrenheit"

    year_data = {} #dictionary key=Year, value=average_temp
    curr_year = datetime.now().year

    #fill year_data
    for i in range(num_years):
        year = curr_year - i - 1  # exclude current year (might be incomplete)
        data = get_yearly_weather(lat, lon, year, temperature_unit)
        #st.write(f"lat={lat}, lon={lon}, temperature_unit={temperature_unit}, year={year}") #for debug
        #st.write(f"data={data}") #for debug
        if data:
            avg_temp = get_average_yearly_weather(data)
            if avg_temp:
                year_data[str(year)] = avg_temp

    return year_data if year_data  else None
