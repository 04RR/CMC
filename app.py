import streamlit as st
import requests
from bs4 import BeautifulSoup
import json


with open("data.json", "r") as f:
    data = json.load(f)["data"]


def get_data(slug):
    base_url = "https://coinmarketcap.com/currencies/NAME/"
    url = base_url.replace("NAME", slug)
    text = requests.get(url).content

    soup = BeautifulSoup(text, "html.parser")
    data = soup.findAll("div", attrs={"class": "iwnVYw"})

    links_list = []
    for div in data:
        links = div.findAll("a")
        for a in links:
            links_list.append(a["href"])
    return list(set(links_list))


slugs = [x["slug"] for x in data]
names = [x["name"] for x in data]

st.title("DYOR")

select = st.selectbox("Select a crypto", slugs + names)

if select in slugs:
    select = select, names[slugs.index(select)]

elif select in names:
    select = slugs[names.index(select)], select

links = get_data(select[0])

if len(links) == 0:
    links = get_data(select[1])

st.subheader(f"Start with the links below!\n")

for link in links:
    st.markdown(f"{link}\n")
