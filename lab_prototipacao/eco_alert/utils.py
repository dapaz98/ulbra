import os
from geopy.geocoders import Nominatim

def get_coordinates(endereco):
    try:
        geo = Nominatim(user_agent="eco_alert")
        location = geo.geocode(endereco)
        return location.latitude, location.longitude
    except:
        return None, None

def save_file(file):
    if not file:
        return ""
    os.makedirs("uploads", exist_ok=True)
    path = os.path.join("uploads", file.name)
    with open(path, "wb") as f:
        f.write(file.read())
    return path
