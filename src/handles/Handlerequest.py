import urllib.request
from ast import literal_eval
import json


class Handlerequest:
    def __init__(self) -> None:
        pass

    def request_city(self, city) -> None:
        response = urllib.request.urlopen(
            f"https://nominatim.openstreetmap.org/search?city={city}&format=json"
        )

        city = literal_eval(response.read().decode("utf-8"))
        coordinates = [city[0]["lat"], city[0]["lon"]]

        return coordinates
