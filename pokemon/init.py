#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import requests
from bs4 import BeautifulSoup
import mysql.connector

db = mysql.connector.connect(host="127.0.0.1", user="root", database="Pokemon")
cursor = db.cursor()

def parse_html():
    url = "https://pokemondb.net/pokedex/all"
    response = requests.get(url)
    html = str(response.content)

    pokemon_site = open("pokemon_site.html", "w")
    pokemon_site.write(html)
    pokemon_site.close()

    soup = BeautifulSoup(html, "html.parser")
    tab = soup.find(id="pokedex")

    for link in tab.find_all("tr"):
        tab1 = []
        for l in link.find_all("td"):
            tab1.append(l.text)
            print(tab1)
parse_html()