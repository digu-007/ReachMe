import math

from geopy import distance
from geopy.geocoders import Nominatim
from datetime import date
from .models import UserInfo


geolocator = Nominatim(user_agent='user')

def calculate_age(born):
    """Calculates age of the user"""
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_distance(a, b):
    """Calculates score according to distance between two cities"""
    if a == None or b == None:
        return 0.0

    source = geolocator.geocode(a)
    destination = geolocator.geocode(b)
    source_coords = (source.latitude, source.longitude)
    destination_coords = (destination.latitude, destination.longitude)
    dist = distance.distance(source_coords, destination_coords).km

    if dist >= 10000:
        return 0.0
    elif dist <= 1:
        return 100.0

    return 100.0 - (math.log(dist, 10) * 25)


def get_age_difference(a, b):
    """Calculates score according to age difference between two users"""
    if a == None or b == None:
        return 0
    difference = abs(calculate_age(a) - calculate_age(b))
    if difference >= 24:
        return 0.0

    return 100.0 - (difference * 25.0 / 6.0)


def get_common_interests(a, b):
    """Calculates score according to common interests between two users"""
    total, found = 0, 0
    for x in a.all():
        total += 1
        for y in b.all():
            if y == x:
                found += 1
                break

    return 100 * float(found) / float(total)



def get_recommendations(user):
    """Returns UserInfo list for the recommendations"""
    users = UserInfo.objects.all()
    logged_user = users.first()
    for cur_user in users:
        if cur_user.user == user:
            logged_user = cur_user
            break

    city = logged_user.city
    date_of_birth = logged_user.date_of_birth
    interests = logged_user.interests

    res = []
    for cur_user in users:
        if cur_user.user == None:
            continue
        if cur_user.user != user:
            dist = get_distance(city, cur_user.city)
            age_difference = get_age_difference(date_of_birth, cur_user.date_of_birth)
            common_interests = get_common_interests(interests, cur_user.interests)
            final_value = dist + age_difference + 2 * common_interests
            res.append((final_value, cur_user.id))
    res.sort()
    res.reverse()

    recommendations = []
    for x in res:
        for y in users:
            if y.id == x[1]:
                value = x[0] / 400.0
                value = value ** (0.2)

                y.match = str(int(math.floor(100 * value)))
                y.save()
                recommendations.append(y)
                break

    return recommendations
