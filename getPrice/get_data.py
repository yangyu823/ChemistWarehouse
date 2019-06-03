#!/usr/bin/python

import os
import requests
from lxml import html
from time import sleep
import mysql.connector
from datetime import datetime
from selenium import webdriver
from fuc_agent import get_agent


# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#   Function to get evidence image base on provided link
def get_image(url):
    name = str((url.split('/')[-1]).replace('-', '_'))
    print('Launching Firefox..')
    # date = (datetime.datetime.now().date())
    browser = webdriver.Firefox()
    browser.get(url)
    # screenshot = browser.save_screenshot("%s(%s).png" % (name, date))
    screenshot_png = browser.get_screenshot_as_png()
    print('Closing Firefox..')
    browser.close()
    return screenshot_png


#   Function to check& update existing record from DB
def check_db(link_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='8889',
                                             database='price_db',
                                             user='root',
                                             password='root')
        sql_insert_query = """ SELECT * FROM `product_cat` WHERE `link_id`=(%s)"""
        # cursor = connection.cursor()
        # result = cursor.execute(sql_insert_query, link_id)
        # connection.commit()
        print((sql_insert_query, link_id))
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into price_db table. {}".format(error))

    # finally:
    #     # closing database connection.
    #     if (connection.is_connected()):
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")


#   Function for insert into database
def insert_db(p_id, p_vendor, p_name, p_price, p_img, time, l_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='8889',
                                             database='price_db',
                                             user='root',
                                             password='root')
        sql_insert_query = """ INSERT INTO `price_history`(`id`, `vendor`, `name`, `price`, `date`, `image`) VALUES (%s,%s,%s,%s,%s,%s)"""
        sql_insert_query2 = """ INSERT INTO `product_cat`(`id`, `vendor`, `name`, `last_update`, `link`, `link_id`) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor = connection.cursor()
        p_info = (p_id, p_vendor, p_name, p_price, time, p_img)
        p_link = 'https://www.chemistwarehouse.com.au/buy/%s' % l_id
        c_info = (p_id, p_vendor, p_name, time, p_link, l_id)
        cursor.execute(sql_insert_query, p_info)
        cursor.execute(sql_insert_query2, c_info)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into price_db table. {}".format(error))

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#   Main function to extract data , image and insert into database
def get_data(url):
    response = requests.get(url, timeout=2, headers={'User-Agent': get_agent()}).text
    selector = html.fromstring(response)
    if (len(selector.xpath('//*[@class="productDetail"]'))) == 0:
        return
    else:
        product_id = ((selector.xpath('//*[@class="product-id"]/text()')[0]).split(':')[-1]).strip()
        product_name = (selector.xpath('//*[@class="product-name"]/h1/text()')[0]).strip()
        product_price = (selector.xpath('//*[@class="Price"]/span/text()')[0]).split("$")[-1]
        capture_time = datetime.now().date().strftime('%Y-%m-%d')
        # -----This is for different vendor-----
        if "chemistwarehouse" in url:
            product_vendor = 'ChemistWarehouse'
        elif "mychemist" in url:
            product_vendor = 'MyChemist'
        else:
            product_vendor = 'Unknow'

        #   Check database for product info
        link_id = link.split('/')[-1]
        check_db(link_id)

        # -----This is for evidence image-----
        product_img = get_image(url)

        #   Insert Into Databse
        insert_db(product_id, product_vendor, product_name, product_price, product_img, capture_time, link_id)

        return True


if __name__ == '__main__':
    link = 'https://www.chemistwarehouse.com.au/buy/65960'
    # link = 'https://www.chemistwarehouse.com.au/buy/65962'
    if get_data(link) is None:
        print("Product not found")
    else:
        print("Product found")
