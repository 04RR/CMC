import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm


with open('crypto_links.json', 'r') as f:
    data = json.load(f)


new_dict = {}

for key, value in data.items():
    if value != []:
        new_dict[key] = list(set(value))

with open('crypto_links_clean.json', 'w') as f:
    json.dump(new_dict, f, indent=4)