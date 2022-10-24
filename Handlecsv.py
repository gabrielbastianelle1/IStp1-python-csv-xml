import csv
import random
import json

class Handlecsv:
    def __init__(self) -> None:
        self.cities = [] 
        self.cities_dict = {}
        self.movie_dict = {}
        self.movies_updated = []
        self.read_csv_cities()
        self.read_csv_movies()
        self.convert_cities_to_array()
        self.change_value_country_for_city()

    def read_csv_movies(self) -> None:
        csv_file = open('./netflix1.csv', newline='')
        self.movie_dict = csv.DictReader(csv_file)

    def read_csv_cities(self) -> None:
        csv_file = open('./cities.csv', newline='')
        self.cities_dict = csv.DictReader(csv_file)

    def convert_cities_to_array(self) -> None:
        for valor in list(self.cities_dict):
            self.cities.append(valor['cities'])

    def change_value_country_for_city(self) -> None:

        for  value in self.movie_dict:
            value['city'] = self.cities[random.randint(0,199)]
            del value['country']
            #print(json.dumps(value, indent=2))          
            self.movies_updated.append(value)

    def write_new_csv(self) -> None:
        new_file = open('netflix_updated.csv','w',newline='')
        fields = ['show_id','type','title','director','date_added','release_year','rating','duration','listed_in','city']
        writer = csv.DictWriter(new_file, fieldnames=fields)

        writer.writeheader()

        for value in self.movies_updated:
            writer.writerow(value)

    def get_movies(self):
        return self.movies_updated       

handle = Handlecsv()