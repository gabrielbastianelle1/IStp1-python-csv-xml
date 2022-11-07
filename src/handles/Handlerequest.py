import urllib.request
from ast import literal_eval
import json


class Handlerequest:
    def __init__(self) -> None:
        self.cities = []
        pass

    def request_all_cities(self, city) -> None:
        response = urllib.request.urlopen(
            f"https://nominatim.openstreetmap.org/search?city={city}&format=json"
        )

        self.cities = literal_eval(response.read().decode("utf-8"))

    def get_random_city(self) -> str:
        self.request_all_cities()

        pass
