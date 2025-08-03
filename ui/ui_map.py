import folium
from streamlit_folium import st_folium

def show_map_for_location(lat: float, lon: float, city: str, country: str):
    """
    this function display map of specific location
    :param lat: latitude
    :param lon: longitude
    :param city: city selected by user
    :param country: country selected by user
    :return:
    """
    m = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], tooltip=f"{city}, {country}").add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)