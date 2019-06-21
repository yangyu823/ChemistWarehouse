#!/usr/bin/python
# import json
import datetime
from selenium import webdriver
from time import sleep


#  Save a screenshot from spotify.com in current directory.
def get_image(url):
    name = str((url.split('/')[-1]).replace('-', '_'))
    print('Launching Firefox..')
    date = (datetime.datetime.now().date())
    print(date)
    browser = webdriver.Firefox()
    browser.get(url)
    sleep(1)
    screenshot = browser.save_screenshot("%s(%s).png" % (name, date))
    screenshot_png = browser.get_screenshot_as_png()
    print('Closing Firefox..')

    browser.close()

if __name__ == '__main__':
    url = 'https://www.chemistwarehouse.com.au/buy/65960/blackmores-omega-triple-concentrated-fish-oil-150-capsules'
    get_image(url)