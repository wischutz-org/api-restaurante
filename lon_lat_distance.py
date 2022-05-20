from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_cood(address):
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


def get_distance(address1, address2):
    geolocator = Nominatim(user_agent="app")
    address1 = geolocator.geocode(address1)
    address2 = geolocator.geocode(address2)

    adress_loc1 = (address1.latitude, address1.longitude)
    adress_loc2 = (address2.latitude, address2.longitude)

    return (geodesic(adress_loc1, adress_loc2))


distancia = get_distance("Mossoró", "Natal")
print(f"A distância entre os locais é de {distancia}")
local = get_cood("Rua José Erasmo de Moura, 470, Alto do Sumaré, Mossoró/RN")
print(local)
