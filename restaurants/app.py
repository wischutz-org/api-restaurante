from fastapi import FastAPI
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


app = FastAPI(title="Restaurants")


@app.get("/rest-cood")
def get_cood(address):
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


@app.get("/rest-distance")
def get_distance(address1, address2):
    geolocator = Nominatim(user_agent="app")
    address1 = geolocator.geocode(address1)
    address2 = geolocator.geocode(address2)

    adress_loc1 = (address1.latitude, address1.longitude)
    adress_loc2 = (address2.latitude, address2.longitude)

    return (geodesic(adress_loc1, adress_loc2)).km
