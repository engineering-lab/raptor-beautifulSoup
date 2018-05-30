from Scripts_v1.crawlers.modules.functions import get_page, produce_listing, access_listing
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

# UNFINISHED - This function should take in access_listing and retrieve product information from table.
def get_item(access_listing): # instead accept access_listing and retrieve all info from tables on product page.
    target = []
    for page_html in access_listing:
        page_soup = Bs(page_html, "lxml")
        refined = []
        refined.append(page_soup)
    print("Retrieving each page item...")
    for elements in refined:
        print(elements)



url='https://www.willi-rothfuss.de/kategorie/uhren/?pa_marke=a-lange-soehne%2Calpina%2Cangelus%2Caudemars-piguet%' \
    '2Cbaume-mercier%2Cblancpain%2Cbreguet%2Cbreitling%2Cbucherer%2Cbulgari%2Cbvlgari%2Ccartier%2Cchanel%2Cchopard%' \
    '2Cchronoswiss%2Ccomor%2Ccorum%2Cdu-bois%2Cdugena%2Cebel%2Ceberhard-co%2Ceterna%2Cferrari%2Cfestina%2Cfortis%' \
    '2Cfranck-muller%2Cgirard-perregaux%2Cglashuette-original%2Cgraham%2Chanhart%2Cheuer%2Chublot%2Ciwc%' \
    '2Cjacques-etoile%2Cjaeger-lecoultre%2Cjunghans%2Cle-blanc%2Cle-phare%2Clongines%2Cmaurice-lacroix%2Cmeistersinger%' \
    '2Cmido%2Cmontblanc%2Cmuehle-nautische%2Cnomos%2Comega%2Corfina%2Coris%2Cpanerai%2Cpatek-philippe%2Cpiaget%' \
    '2Cporsche-design%2Cpriosa%2Crado%2Crainer-band%2Crolex%2Csinn%2Csonstige%2Ctag-heuer%2Ctissot%2Ctudor%' \
    '2Culysse-nardin%2Cunion-glashuette%2Cuniversal-geneve%2Cvacheron-constantin%2Cwempe%2Cwittnauer%2Czenith'


#print(get_item(get_page(url)))
#print(access_listing(produce_listing(get_page(url)))) # TEST ACCESS_LISTING
print(produce_listing(get_page(url)))  # TEST PRODUCE_LISTING
#print(get_item(access_listing(produce_listing(get_page(url))))) # MAIN ... wtf

