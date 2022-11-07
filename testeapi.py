import urllib.request
from ast import literal_eval
import json

response = urllib.request.urlopen(
    "https://nominatim.openstreetmap.org/search?country=United_Kingdom&format=json"
)

data = literal_eval(response.read().decode("utf-8"))

print(json.dumps(data[0], indent=2))
