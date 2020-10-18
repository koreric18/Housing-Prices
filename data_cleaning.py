# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:01:08 2020

@author: ilike
"""

import pandas as pd

df = pd.read_csv('HousingPrices_Unfiltered.csv')

# Remove the address?
# Parse the zipcodeout of the title link
# make columns in the following format:
    # Zip Code, Sold date, Price, Bed, bath

#df.info()

df.isnull().sum(axis = 0)

#zipcode = df['Title_link'].apply(lambda x: x.split('-')[6])