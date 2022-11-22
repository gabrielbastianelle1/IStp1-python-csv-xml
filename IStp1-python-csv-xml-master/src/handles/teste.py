import pandas as pd
import xml.etree.ElementTree as ET
import json

from Handlecsv import Handlecsv

""" ds = pd.read_csv("./netflix1.csv", nrows=10000)
df = ds.groupby(["rating"])["rating"].count().value_counts()

total = ds["country"].unique()

print(len(total)) """


# pandas parte
# pd.set_option('display.max_rows', None)
ds = pd.read_csv("./csvFiles/netflix1.csv", nrows=10)
df = ds.groupby(["type"])["type"].count()

# xml part
movies = ET.Element("movies")

for campo in df.keys():
    tipo = ET.Element("type", attrib={"type": f"{campo}"})
    movies.append(tipo)

##########################################


df = ds.groupby(["release_year", "type"])["type"].count()

for campo in df.keys():
    tipos = movies.findall(f'.//type[@type="{campo[1]}"]')
    for elem in movies.findall(".//type"):
        for tipo in tipos:
            if elem == tipo:
                ano = ET.Element("release_year", attrib={"release_year": f"{campo[0]}"})
                tipo.append(ano)


############################################


df = ds.groupby(["release_year", "type", "country"])["type"].count()

print(df)

for campo in df.keys():
    type = movies.findall(f".//type[@type='{campo[1]}']")
    year = type[0].findall(f".//release_year[@release_year='{campo[0]}']")

    country = ET.Element("country", attrib={"country": f"{campo[2]}"})

    year[0].append(country)

############################################

handle = Handlecsv()
filmes = handle.get_movies()


for filme in filmes:
    tipo = movies.findall(f".//type[@type='{filme['type']}']")
    ano = tipo[0].findall(f".//release_year[@release_year='{filme['release_year']}']")
    pais = ano[0].findall(f".//country[@country='{filme['country']}']")

    movie = ET.Element("movie", attrib={"id": f'{filme["show_id"]}'})

    city = ET.SubElement(
        movie, "city", attrib={"lat": f'{filme["lat"]}', "lon": f'{filme["lon"]}'}
    ).text = f'{filme["city"]}'

    ET.SubElement(movie, "listed_in").text = f'{filme["listed_in"]}'
    ET.SubElement(movie, "title").text = f'{filme["title"]}'
    ET.SubElement(movie, "rating").text = f'{filme["rating"]}'
    ET.SubElement(movie, "score").text = f'{filme["score"]}'
    ET.SubElement(movie, "duration").text = f'{filme["duration"]}'

    pais[0].append(movie)


ET.indent(tree=movies, space="\t", level=0)


xml_file = ET.ElementTree(movies)
xml_file.write("movies.xml", encoding="utf-8", xml_declaration=True)
