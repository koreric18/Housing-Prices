# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:43:19 2020

@author: ilike
"""

import re
import sys
import os
from selenium import webdriver

chromedriver = "~/Desktop/chromedriver.exe" # path to the chromedriver executable
chromedriver = os.path.expanduser(chromedriver)
print('chromedriver path: {}'.format(chromedriver))
sys.path.append(chromedriver)
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.zillow.com/homedetails/520-E-Escalon-Ave-Fresno-CA-93710/18704874_zpid/')
result = re.findall('(?<=Home Value:\s)\$[\d,\s]+', driver.page_source)[0]