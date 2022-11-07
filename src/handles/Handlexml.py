import pandas as pd
import xml.etree.ElementTree as ET

from Handlecsv import Handlecsv


class Handlexml:
    def __init__(self) -> None:
        self.csv = Handlecsv()
        self.filmes = self.csv.get_movies()

        self.movies = ET.Element("movies")

        self.dataset = pd.DataFrame()
        self.series = pd.Series()

        self.read_csv()
        self.create_types_tag()
        self.create_release_year_tag()
        self.create_country_tag()
        self.create_movie_tag()
        self.create_xml()

    def read_csv(self) -> None:
        self.dataset = pd.read_csv("./csvFiles/netflix1.csv", nrows=10000)

    def create_types_tag(self) -> None:
        self.series = self.dataset.groupby(["type"])["type"].count()

        for campo in self.series.keys():
            tipo = ET.Element("type", attrib={"type": f"{campo}"})
            self.movies.append(tipo)

    def create_release_year_tag(self) -> None:
        self.series = self.dataset.groupby(["release_year", "type"])["type"].count()

        for campo in self.series.keys():
            tipos = self.movies.findall(f'.//type[@type="{campo[1]}"]')
            for elem in self.movies.findall(".//type"):
                for tipo in tipos:
                    if elem == tipo:
                        ano = ET.Element(
                            "release_year", attrib={"release_year": f"{campo[0]}"}
                        )
                        tipo.append(ano)

    def create_country_tag(self) -> None:
        self.series = self.dataset.groupby(["release_year", "type", "country"])[
            "type"
        ].count()

        for campo in self.series.keys():
            anos = self.movies.findall(f'.//release_year[@release_year="{campo[0]}"]')
            for elem in self.movies.findall(".//release_year"):
                for ano in anos:
                    if elem == ano:
                        pais = ET.Element("country", attrib={"country": f"{campo[2]}"})
                        elem.append(pais)

    def create_movie_tag(self) -> None:
        for filme in self.filmes:
            tipo = self.movies.findall(f".//type[@type='{filme['type']}']")
            ano = tipo[0].findall(
                f".//release_year[@release_year='{filme['release_year']}']"
            )
            pais = ano[0].findall(f".//country[@country='{filme['country']}']")

            movie = ET.Element("movie", attrib={"id": f'{filme["show_id"]}'})

            ET.SubElement(
                movie,
                "city",
                attrib={"lat": f'{filme["lat"]}', "lon": f'{filme["lon"]}'},
            ).text = f'{filme["city"]}'

            ET.SubElement(movie, "listed_in").text = f'{filme["listed_in"]}'
            ET.SubElement(movie, "title").text = f'{filme["title"]}'
            ET.SubElement(movie, "rating").text = f'{filme["rating"]}'
            ET.SubElement(movie, "score").text = f'{filme["score"]}'
            ET.SubElement(movie, "duration").text = f'{filme["duration"]}'

            pais[0].append(movie)

    def create_xml(self) -> None:
        ET.indent(tree=self.movies, space="\t", level=0)

        xml_file = ET.ElementTree(self.movies)
        xml_file.write("movies.xml", encoding="utf-8", xml_declaration=True)


teste = Handlexml()
