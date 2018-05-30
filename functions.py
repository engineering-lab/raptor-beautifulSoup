import csv
import urllib
import lxml
import re
import requests
from bs4 import BeautifulSoup as Bs
from bs4 import SoupStrainer as Strain

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

#______________________________________________________________________________________________________________________
# This function accesses each href url and returns all the html content of all the individual products.
def access_listing(produce_listing):
    print("Opening each page...")
    req_list = []
    for value in produce_listing:
        req_list.append(value)

    print(req_list)

    for url in req_list:
        page_html = requests.get(url, headers=headers)
        item_html = page_html.text
        item_soup = Bs(item_html, "lxml")
        item_content = []
        item_content.append(item_soup.prettify())

    for req in item_content:
        print(req)
        #yield(req)
#____________________________________________________________________________________________________________________
#This function returns the href url of each product on the listings page.
def produce_listing(get_page):
    txt = open("store.txt", "w+")
    print("Retrieving listings...")
    soup = Bs(get_page, "lxml")
    url_staging = []
    for h in soup.select('.product-card .product-card__image a'):
        url_staging.append(h)
    txt.write(str(url_staging))
    txt.close()
    with open('store.txt', 'r') as f:
        item_url = []
        for link in Bs(f.read(), "lxml", parse_only=Strain('a')):
            if link.has_attr('href'):
                item_url.append(link['href'])

    for item in item_url:
        print(item)
        yield(item)
#_____________________________________________________________________________________________________________________
# This function requests target url and grabs all the html data and returns the content.
def get_page(url):
    print("Retrieving page...")
    r = requests.get(url, headers=headers)
    html = r.text
    soup = Bs(html, "lxml")
    content = soup.prettify()
    return content

