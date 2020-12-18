from geopy import distance
from geopy.geocoders import Nominatim


def get_distance(a, b):
    geolocator = Nominatim(user_agent='user')
    source = geolocator.geocode(a)
    destination = geolocator.geocode(b)
    source_coords = (source.latitude, source.longitude)
    destination_coords = (destination.latitude, destination.longitude)
    return distance.distance(source_coords, destination_coords).km
