'''
Web Scraper: Extract data from websites using libraries like Beautiful Soup or Scrapy.
'''

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.google.com/")     # I just want to extract data from this website.
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
