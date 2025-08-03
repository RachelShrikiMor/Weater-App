from datetime import datetime
from timezonefinderL import TimezoneFinder
import pytz

# Create an instance
tf = TimezoneFinder()

def get_timezones_by_country_code(country_code):
    """
    this function return the timezone by country code(alfa_2)
    example for call: get_timezones_by_country_code('IL')
    """
    timezones = pytz.country_timezones.get(country_code)


def display_date_time(longitude,latitude):
    """
    this function returns the user_timezone
    the function get user location data: longitude and latitude
    tf.timezone_at(lng,lat) create the country_name/City_name format for pytz
    like 'Europe/London'

    comment: every country and city has different timezones
    """
    user_timezone = tf.timezone_at(lng=longitude, lat=latitude)
    # Fetch current date and time in user's timezone
    user_time = datetime.now(pytz.timezone(user_timezone))
    formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
    return formatted_user_time




