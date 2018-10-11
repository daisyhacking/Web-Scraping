# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:14:34 2018

@author: 64254
"""

import webbrowser

new = 2

tabUrl = "http://google.com/?#q=";
term = "london cordination";

webbrowser.open(tabUrl + term, new = new);


https://www.google.com/search?q=London%20Coordinates&cad=h

import requests
from bs4 import BeautifulSoup

page= requests.get('https://www.google.com/search?q=London%20Coordinates&cad=h')
soup = BeautifulSoup(page.text, 'html.parser')

cordinates = soup.find_all("div", class_= "R8KuR")

