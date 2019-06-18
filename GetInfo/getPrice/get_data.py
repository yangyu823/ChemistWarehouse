#!/usr/bin/python

import os
import requests
from lxml import html
from time import sleep
import mysql.connector
import json
from datetime import datetime
from selenium import webdriver
from GetInfo.getPrice.fuc_agent import get_agent

# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

connection = mysql.connector.connect(host='localhost',
                                     port='8889',
                                     database='price_db',
                                     user='root',
                                     password='root')
cursor = connection.cursor()


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


def insert_db(p_id, p_vendor, p_name, p_price, time, l_id, update, create, p_img):
    #   Create New Record
    if not update and create:
        try:
            sql_create_query = """ INSERT INTO `product_history`(`product_id`, `vendor`, `name`, `price`, `date`) VALUES (%s,%s,%s,%s,%s)"""
            sql_create_query2 = """ INSERT INTO `product_cat`(`product_id`, `vendor`, `name`, `last_update`, `link`, `link_id`,`prod_img`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            p_info = (p_id, p_vendor, p_name, p_price, time)
            p_link = 'https://www.chemistwarehouse.com.au/buy/%s' % l_id
            c_info = (p_id, p_vendor, p_name, time, p_link, l_id, p_img)
            cursor.execute(sql_create_query, p_info)
            cursor.execute(sql_create_query2, c_info)
            connection.commit()
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured

    #   Update Existing Record
    elif update and not create:
        try:
            sql_update_query = """ INSERT INTO `product_history`(`product_id`, `vendor`, `name`, `price`, `date`) VALUES (%s,%s,%s,%s,%s)"""
            sql_update_query2 = """ UPDATE `product_cat` SET last_update = %s WHERE link_id = %s """
            p_info = (p_id, p_vendor, p_name, p_price, time)
            c_info = (time, l_id)
            cursor.execute(sql_update_query, p_info)
            cursor.execute(sql_update_query2, c_info)
            connection.commit()
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
    elif not update and not create:
        print("record up to date")
    else:
        print("Impossible")


def get_data(vendor, product_id, product_name, product_img):
    record_final = {}
    try:
        sql_get_query = """SELECT `price`,`date` FROM `product_history` WHERE product_id = %s AND vendor = %s"""
        #   cursor.execute(sql_insert_query, (link_id,))  standard format:  (variable,)     !!!!!
        cursor.execute(sql_get_query, (product_id, vendor))
        records = cursor.fetchall()
        result = {}
        history = {}
        result["id"] = product_id
        result["vendor"] = vendor
        result["name"] = product_name
        result["img"] = product_img
        for row in records:
            history[row[1].strftime("%b-%d-%Y")] = row[0]
        result["price_history"] = history
        record_final = json.dumps(result)
        # print(record_final)
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
    return result


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

    response = requests.get(url, timeout=2, headers={'User-Agent': get_agent()}).text
    selector = html.fromstring(response)

    #   Link page validation
    if (len(selector.xpath('//*[@class="productDetail"]'))) == 0:
        return {"End Result - Product Not Found"}
    else:
        product_id = ((selector.xpath('//*[@class="product-id"]/text()')[0]).split(':')[-1]).strip()
        product_name = (selector.xpath('//*[@class="product-name"]/h1/text()')[0]).strip()
        product_price = (selector.xpath('//*[@class="Price"]/span/text()')[0]).split("$")[-1]
        capture_time = datetime.now().date().strftime('%Y-%m-%d')
        product_img = (selector.xpath('//*[@class="image_enlarger"]/@href')[0])
        #   Check database for product info
        #   Condition check for next step
        try:
            sql_check_query = """ SELECT last_update FROM `product_cat` WHERE link_id = %s AND vendor =%s"""
            #   cursor.execute(sql_insert_query, (link_id,))  standard format:  (variable,)     !!!!!
            cursor.execute(sql_check_query, (link_id, product_vendor))
            records = cursor.fetchall()
            if records:
                for row in records:
                    if row[0] > (datetime.now().date()):
                        return {"End Result - Impossible"}
                    elif row[0] < (datetime.now().date()):
                        #   Outdated Record
                        insert_db(p_id=product_id, p_vendor=product_vendor, p_name=product_name, p_price=product_price,
                                  time=capture_time, l_id=link_id, update=True, create=False, p_img=product_img)
                        #   pull the history data
                        return get_data(product_vendor, product_id, product_name, product_img)
                    else:
                        #   Record up to date
                        #   pull the history data
                        return get_data(product_vendor, product_id, product_name, product_img)

            else:
                # Insert Into Databse
                insert_db(p_id=product_id, p_vendor=product_vendor, p_name=product_name, p_price=product_price,
                          time=capture_time, l_id=link_id, update=False, create=True, p_img=product_img)
                return {"End Result No Current Record!"}

        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            return {"End Result - Failed inserting record.  {}".format(error)}

        finally:
            # closing database connection.
            if connection.is_connected():
                cursor.close()
                connection.close()
                # print("MySQL connection is closed")

            # -----This is for evidence image(Options)-----
            # product_img = get_image(url)

# if __name__ == '__main__':
#     link = 'https://www.chemistwarehouse.com.au/buy/65966'
#     # link = 'https://www.chemistwarehouse.com.au/buy/65967'
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
#
#     print(check_data(link))
