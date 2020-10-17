# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:45:43 2020

@author: ilike
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:37:47 2020

@author: Eric
"""
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re

chromedriver = "~/Desktop/chromedriver.exe" # path to the chromedriver executable
chromedriver = os.path.expanduser(chromedriver)
print('chromedriver path: {}'.format(chromedriver))
sys.path.append(chromedriver)
driver = webdriver.Chrome(chromedriver)

zillow_fresno_url = "https://www.trulia.com/sold/Fresno,CA/"
driver.get(zillow_fresno_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
listings = soup.find_all('div', 'a',
                         {'class':"Box-sc-8ox7qa-0",
                         'data-testid':'home-card-sale'}
                         )
print(listings)
#print(listings[:1])
#house_links = [row['href'] for row in listings]
#fixed_links = list(dict.fromkeys(house_links))
"""
def get_house_links(url, driver, pages=20):
    house_links=[]
    driver.get(url)
    for i in range(pages):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        listings = soup.find_all("a", class_="list-card-link")
        page_data = [row['href'] for row in listings]
        house_links.append(page_data)
        time.sleep(np.random.lognormal(0,1))
        next_button = soup.find_all("a", class_="Button-wpcbcc-0")
        next_button_link = ['https://www.zillow.com'+row['href']+str(i)+'_p/?searchQueryState=%7B"usersSearchTerm"%3A"Fresno%20County%2C%20CA"%2C"mapBounds"%3A%7B"west"%3A-121.58423757812501%2C"east"%3A-117.69507742187501%2C"south"%3A35.22204153291143%2C"north"%3A38.25002342226141%7D%2C"mapZoom"%3A8%2C"regionSelection"%3A%5B%7B"regionId"%3A1018%2C"regionType"%3A4%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"pmf"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"sort"%3A%7B"value"%3A"globalrelevanceex"%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"rs"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%2C"pagination"%3A%7B"currentPage"%3A2%7D%7D' for row in next_button]
        if i<19:
            print(next_button_link[0])
            driver.get(next_button_link[0])
        
    return house_links

get_house_links(zillow_fresno_url, driver)
"""

def get_html_data(url, driver):
    driver.get(url)
    time.sleep(np.random.lognormal(0,1))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def get_price(soup):
    try:
        obj = soup.find("div", class_='Text__TextBase-sc-1i9uasc-0-div Text__TextContainerBase-sc-1i9uasc-1 qAaUO')
        price = obj[0]
        return price
    except:
        return np.nan
    
def get_sale_date(soup):
    try:
        obj = soup.find_all("span",class_='ckNXCT')
        sale_date = obj[0].text.split()[0]
        return sale_date
    except:
        return 'None'
 
def get_lot_size(soup):
    try:
        lot_size_regex = re.compile('Lot:')
        obj = soup.find(text=lot_size_regex).find_next()
        return obj.text
    except:
        return 'None'
def get_address(soup):
    try:
        obj = soup.find("address",class_="list-card-addr").text.split(',')
        address = obj[0]
        return address
    except:
        return 'None'
def get_city(soup):
    try:
        obj = soup.find("address",class_="list-card-addr").text.split(',')
        city = obj[1]
        return city
    except:
        return 'None'
    
def get_zip(soup):
    try:
        obj = soup.find("address",class_="list-card-addr").text.split(',')
        list = obj[2].split()
        zip_code = list[1]
        return zip_code
    except:
        return 'None'
def get_num_beds(soup):
    try:
        obj = soup.find_all("span",class_='ds-bed-bath-living-area')
        beds = obj[0].text.split()[0]
        return beds
    except:
        return 'None'
    
def get_num_baths(soup):
    try:
        obj = soup.find_all("span",class_='ds-bed-bath-living-area')
        beds = obj[1].text.split()[0]
        return beds
    except:
        return 'None'
    
def get_floor_size(soup):
    try:
        obj = soup.find_all("span",class_='ds-bed-bath-living-area')
        floor_size_string = obj[2].text.split()[0]
        floor_size = floor_size_string.replace(",","")
        return floor_size
    except:
        return 'None'
    
def get_year_built(soup):
    try:
        objs = soup.find_all("span",class_='ds-body ds-home-fact-value')
        built = objs[1].text.split()[0]
        return built
    except:
        return 'None'
    
def get_overview_data(soup):
    try:
        obj = soup.find("div",class_="Text-aiai24-0")
        overview = obj[0]
        return overview
    except:
        return 'None'


def flatten_list(house_links):
    house_links_flat=[]
    for sublist in house_links:
        for item in sublist:
            house_links_flat.append(item)
    return house_links_flat


def get_house_data(driver,house_links_flat):
    house_data = []
    for link in house_links_flat:
        print(link)
        soup = get_html_data(link,driver)
        address = get_address(soup)
        city = get_city(soup)
        zip_code = get_zip(soup)
        beds = get_num_beds(soup)
        baths = get_num_baths(soup)
        floor_size = get_floor_size(soup)
        lot_size = get_lot_size(soup)
        year_built = get_year_built(soup)
        sale_date = get_sale_date(soup)
        price = get_price(soup)
        house_data.append([address,city,zip_code,beds,baths,floor_size,lot_size,year_built,sale_date,price])
        
    return house_data
"""
#house_links_flat = flatten_list(house_links)
house_data = get_house_data(driver,fixed_links)

file_name = "%s_%s.csv" % (str(time.strftime("%Y-%m-%d")), 
                           str(time.strftime("%H%M%S")))
columns = ["address", "city", "zip", "bedrooms", "bathrooms", "floor_size", "lot_size", "year_built", "sale_date", "sale_price"]
pd.DataFrame(house_data, columns = columns).to_csv(
    file_name, index = False, encoding = "UTF-8"
)

"""