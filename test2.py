#!/usr/bin/python

import os
import requests
from lxml import html
from time import sleep
import mysql.connector
import json
from datetime import datetime
from selenium import webdriver
from PriceTracker.backend.getPrice.fuc_agent import get_agent

# from fuc_agent import get_agent

# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

connection = mysql.connector.connect(host='localhost',
                                     port='8889',
                                     database='price_db',
                                     user='root',
                                     password='root')
cursor = connection.cursor()


#   Main function to extract data , image and insert into database
def check_data(url):
    # -----This is for Reformat URL && different vendor-----
    if "chemistwarehouse" in url:
        product_vendor = 'ChemistWarehouse'
        temp_array = url.split("/")
        temp_count = 0

        while temp_count < len(temp_array):
            if temp_array[temp_count] == "buy":
                link_id = temp_array[temp_count + 1]
                url = "https://www.chemistwarehouse.com.au/buy/" + temp_array[temp_count + 1]
            temp_count += 1

    elif "mychemist" in url:
        product_vendor = 'MyChemist'
    else:
        product_vendor = 'Unknow'

    #   Reformat URL:
    if url.startswith("www"):
        url = "https://" + url
    try:
        response = requests.get(url, timeout=2, headers={'User-Agent': get_agent()}).text
        selector = html.fromstring(response)
    except:
        return "Error"

    print(url)

    #   Link page validation

    # try:
    #     if (len(selector.xpath('//*[@class="productDetail"]'))) == 0:
    #         return {"Result": "Product Not Found"}
    #     else:
    #         return ("WTF")
    # except:
    #     return ("ERROR with WebAddress")


if __name__ == '__main__':
    link = 'https://www.chemistware.com'
    # link = 'https://www.chemistwarehouse.com.au/buy/65967'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65968'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65969'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65960'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65970'
    #     # link = 'www.chemistwarehouse.com.au/buy/65964'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65961/sdlfjsdf'
    #
    #     # Product not found:
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65965'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65962'
    print(check_data(link))
