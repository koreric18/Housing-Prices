# Exploratory Analysis on Fresno Housing Prices

In this project, we explore homes sold in the year 2019 and 2020 in Fresno and Clovis. Housing prices are affected by many different factors. In this analysis,
we aim to analyze housing prices in Fresno using their zipcode. We engineer two new features, the number of parks located within a specific zipcode and the number of 
registered sexual offenders living within specific zipcodes. Additionally, we trained a machine learning model to predict the price of a home located in Fresno.

## Motivation - why is this important?

![Traintrack image](/Images/median.png)

We recognized that there are disproportionate gaps of wealth throughout regional neighborhoods in Fresno. This can be traced back from a historical standpoint. The photo
above indicates the median price of houses. In the 1970s, people of color were not allowed to be on the east side of the train tracks (the dotted line) after sunset.
So, people of color were forced to live on the west side of the train tracks. Due to the lack of funds being allocated to this area, it continues to be a low-income area
where drugs and violence are prominent. 

Ideally, analyzing this type of data is essential because it is important to understand why housing prices differ dependent on the zipcode one resides in. Additionally,
these type of insights can influence policy change so leaders in our cities can better serve their people.

## The data

The housing prices were scraped using an API. While there was an attempt to scrape the housing data off of websites such as Zillow and Redfin using tools like Selenium, 
these websites are notorious for preventing one from using scripts to automate the scraping of their data. Ideally, this type of data should be available to the public;
however, Fresno County does not provide this data. 

