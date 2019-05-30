#!/usr/bin/python

import os
import requests
import datetime
from lxml import html
from time import sleep
from selenium import webdriver
from get_agent import get_agent


# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_image(url):
    name = str((url.split('/')[-1]).replace('-', '_'))
    print('Launching Firefox..')
    date = (datetime.datetime.now().date())
    print(date)
    browser = webdriver.Firefox()
    browser.get(url)
    # screenshot = browser.save_screenshot("%s(%s).png" % (name, date))
    screenshot_png = browser.get_screenshot_as_png()
    print('Closing Firefox..')
    browser.close()
    return screenshot_png


def get_data(url):
    response = requests.get(url, timeout=2, headers={'User-Agent': get_agent()}).text
    selector = html.fromstring(response)
    product_id = ((selector.xpath('//*[@class="product-id"]/text()')[0]).split(':')[-1]).strip()
    product_name = (selector.xpath('//*[@class="product-name"]/h1/text()')[0]).strip()
    product_price = (selector.xpath('//*[@class="Price"]/span/text()')[0]).split("$")[-1]
    capture_time = datetime.datetime.now().date()

    # -----This is for evidence image-----
    # product_img = get_image(url)

    if "chemistwarehouse" in url:
        product_vendor = 'ChemistWarehouse'
    elif "mychemist" in url:
        product_vendor = 'MyChemist'
    else:
        product_vendor = 'Unknow'

    print(product_name)


if __name__ == '__main__':
    link = 'https://www.chemistwarehouse.com.au/buy/65960/blackmores-omega-triple-concentrated-fish-oil-150-capsules'
    get_data(link)
