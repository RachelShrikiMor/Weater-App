import json
import os
from typing import Any

settings: dict[str, Any]
SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE) and os.path.getsize(SETTINGS_FILE) > 0:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {"units": "metric", "language": "English", "dark_mode": False}

def save_settings(user_settings: dict[str, Any]):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(user_settings, f, indent=4)

def get_default_location():
    user_settings = load_settings()
    return user_settings.get("default_location", None)

def set_default_location(country: str, city: str):
    user_settings = load_settings()
    user_settings["default_location"] = {"country": country, "city": city}
    save_settings(user_settings)

def get_units():
    user_settings = load_settings()
    return user_settings.get("units", "metric")

def set_units(units: str):
    user_settings = load_settings()
    user_settings["units"] = units
    save_settings(user_settings)

def get_language():
    user_settings = load_settings()
    return user_settings.get("language", None)


def delete_favorite(index):
    user_settings = load_settings()
    favorites = user_settings.get("favorite_locations", [])
    #favorites = get_favorite_locations()
    if 0 <= index < len(favorites):
        del favorites[index]
        if favorites: # chk if still have values in list after deletion
            user_settings["favorite_locations"] = favorites
        else:
            # List is empty → remove the key entirely
            user_settings.pop("favorite_locations", None)
        save_settings(user_settings)

def add_favorite_location(country: str, city: str) -> None:
    user_settings = load_settings()
    if not isinstance(user_settings.get("favorite_locations"), list):
        user_settings["favorite_locations"] = []

    # Avoid duplicates
    new_fav = {"country": country, "city": city}
    if new_fav not in user_settings["favorite_locations"]:
        user_settings["favorite_locations"].append(new_fav)
        save_settings(user_settings)

def get_favorite_locations() -> list[dict[str, str]]:
    user_settings = load_settings()
    return user_settings.get("favorite_locations", [])

