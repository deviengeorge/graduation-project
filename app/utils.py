import math


def radians(degress):
    return degress * math.pi / 180


def haversine(lat1, lon1, lat2, lon2):
    earth_radius = 6371  # radius of earth in Km
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    a = math.pow(math.sin(dLat / 2), 2) + \
        math.cos(radians(lat1)) * \
        math.cos(radians(lat2)) * \
        math.pow(math.sin(dLon / 2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    return distance
