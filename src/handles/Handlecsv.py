import csv
import random
import json

from .Handlerequest import Handlerequest


class Handlecsv:
    def __init__(self, total_lines) -> None:
        self.total_lines=total_lines

        self.handlerequest = Handlerequest()
        self.cities = []
        self.cities_dict = {}
        self.movie_dict = {}
        self.movies_updated = []
        self.read_csv_cities()
        self.read_csv_movies()
        self.convert_cities_to_array()
        self.update_movies()

    def read_csv_movies(self) -> None:
        csv_file = open("./csvFiles/netflix1.csv", newline="")
        self.movie_dict = csv.DictReader(csv_file)

    def read_csv_cities(self) -> None:
        csv_file = open("./csvFiles/cities.csv", newline="")
        self.cities_dict = csv.DictReader(csv_file)
        self.total_cities = 100

    def remove_special_characters(self, value: str) -> str:
        special_characters = ["@", "#", "$", "*", "&"]
        normal_string = value

        for i in special_characters:
            normal_string = normal_string.replace(i, "and")

        return normal_string

    def convert_cities_to_array(self) -> None:
        for valor in list(self.cities_dict):
            self.cities.append(valor["cities"])

    def add_random_score_value(self) -> float:
        return round(random.uniform(3, 10), 1)

    def update_movies(self) -> None:

        all_lines = list(self.movie_dict)

        for i in range(0, self.total_lines):
            all_lines[i]["city"] = self.cities[random.randint(0, self.total_cities)]
            all_lines[i]["listed_in"] = self.remove_special_characters(
                all_lines[i]["listed_in"]
            )
            all_lines[i]["title"] = self.remove_special_characters(all_lines[i]["title"])
            all_lines[i]["score"] = self.add_random_score_value()

            lat, lon = self.handlerequest.request_city(all_lines[i]["city"])
            all_lines[i]["lat"] = lat
            all_lines[i]["lon"] = lon

            print(json.dumps(all_lines[i], indent=2))

            self.movies_updated.append(all_lines[i])

    def write_new_csv(self) -> None:
        new_file = open("netflix_updated.csv", "w", newline="")
        fields = [
            "show_id",
            "type",
            "title",
            "director",
            "country",
            "date_added",
            "release_year",
            "rating",
            "duration",
            "listed_in",
            "city",
        ]
        writer = csv.DictWriter(new_file, fieldnames=fields)

        writer.writeheader()

        for value in self.movies_updated:
            writer.writerow(value)

    def get_movies(self):
        return self.movies_updated
