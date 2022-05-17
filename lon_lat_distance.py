from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="app")

# Insere os dois locais para comparação de distância
local1 = input("Digite o primeiro local: ")
local2 = input("Digite o segundo local: ")

local1 = geolocator.geocode(local1)
local2 = geolocator.geocode(local2)

# Mostra na tela as latitudes/longitudes dos dois locais
print(f"Latitude L1: {local1.latitude} / Longitude L1: {local1.longitude}")
print(f"Latitude L2: {local2.latitude} / Longitude L2: {local2.longitude}")

Loc1_lat, Loc1_lon = (local1.latitude), (local1.longitude)
Loc2_lat, Loc2_lon = (local2.latitude), (local2.longitude)

localizacao1 = (Loc1_lat, Loc1_lon)
localizacao2 = (Loc2_lat, Loc2_lon)

# Mostra na tela a distância entre os dois locais
distancia = (geodesic(localizacao1, localizacao2).km)
print(f"A distâncie entre os locais é de: {distancia}kms.")
