import pandas as pd
import xml.etree.ElementTree as ET
import json

from Handlecsv import Handlecsv

# pandas parte
#pd.set_option('display.max_rows', None)
ds = pd.read_csv('./netflix1.csv', nrows=10000)
df = ds.groupby(['type'])['type'].count()

print('teste')
# xml part
""" movies = ET.Element('movies')

for campo in df.keys():
  tipo = ET.Element('type' , attrib= {'type' : f'{campo}'})
  movies.append(tipo)

df = ds.groupby(['release_year','type'])['type'].count()

for campo in df.keys():
  tipos = movies.findall(f'.//type[@type="{campo[1]}"]')
  for elem in movies.findall('.//type'):
    for tipo in tipos:
      if(elem == tipo):
        ano = ET.Element('release_year', attrib={'release_year' : f'{campo[0]}'})
        tipo.append(ano)
    
df = ds.groupby(['release_year','type','director'])['type'].count()

for campo in df.keys():
  anos = movies.findall(f'.//release_year[@release_year="{campo[0]}"]')
  for elem in movies.findall('.//release_year'):
    for ano in anos:
      if(elem == ano):
        
        
        diretor = ET.Element('director', attrib={'director' : f'{campo[2]}'})
        elem.append(diretor)

df = ds.groupby(['release_year','director'])['director'].count()


for campo in df.keys():
  diretores = movies.findall(f'.//director[@director="{campo[1]}"]')
  for elem in movies.findall('.//director'):
    for diretor in diretores:
      if(elem == diretor):
        diretor = ET.Element('movie', attrib={'director' : f'teste'})
        elem.append(diretor)

ET.indent(tree=movies, space='\t' ,level=0)

xml_file = ET.ElementTree(movies)
xml_file.write('teste.xml', encoding='utf-8', xml_declaration=True) """


handle = Handlecsv()
filmes = handle.get_movies()
