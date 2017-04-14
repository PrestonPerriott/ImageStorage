import requests
from bs4 import BeautifulSoup
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from textblob import TextBlob
import pyzillow
import re
import csv
import pandas
import matplotlib.pyplot as plt
from collections import OrderedDict



Address = 'http://www.marijuana.com/strains/'
response = requests.get(Address)
HTMLContent = response.content
PrettyHTML = BeautifulSoup(HTMLContent)



objects = []

for object in PrettyHTML.find_all('img', {'itemprop' : 'image' }):
    objects.append(object)
print(objects)

for thing in objects:
    print(thing)

x  = len(objects)
print(x)
    #finds all the src inside of the img tags

#range necessary to iterate through an integer
array = []
for i in range(x):

    #array -> dict
    NEWNEW = PrettyHTML.find_all('img')[i]['src']
    print(NEWNEW)
    array.append(NEWNEW)

with open('strainsAgain.csv', 'w') as out:
    writer = csv.writer(out)
    for key in array:
        writer.writerow([key])









