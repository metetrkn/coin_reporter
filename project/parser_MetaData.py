import json
import requests
from PIL import Image
from io import BytesIO

# Load the ids of currincies which gone import their logos
with open('./curr_ids.txt') as f:
    curr_ids = f.read()

curr_ids = curr_ids.strip("[]") # removing squared brackets from string data
curr_ids_list = curr_ids.split(",") # spliting the string into a list of strings

# base url to scratch coins logo
url_logo = "https://s2.coinmarketcap.com/static/img/coins/64x64/{id}.png"

for id in curr_ids_list:
    url = url_logo.replace("{id}", id)
    response_logo = requests.get(url)
    img = Image.open(BytesIO(response_logo.content))
    img.save(f'../logos/{id}.png')

