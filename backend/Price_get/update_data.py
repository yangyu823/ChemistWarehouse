#!/usr/bin/python

import os
import requests
from lxml import html
from time import sleep
import mysql.connector
import json
from backend.Price_get.get_data import check_data
# from get_data import check_data
from datetime import datetime
from selenium import webdriver


def get_list():
    connection = mysql.connector.connect(host='localhost',
                                         port='8889',
                                         database='price_db',
                                         user='root',
                                         password='root')
    cursor = connection.cursor()
    url_list = []
    try:
        sql_get_list = """SELECT `link` FROM `product_cat` WHERE `last_update`<cast(now() as date)"""
        cursor.execute(sql_get_list)
        records = cursor.fetchall()
        for row in records:
            url_list.append(row[0])
        return url_list
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured

    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
    return url_list

def update_price(list):
    for link in list:
        # print(link)
        check_data(link)
        print(link + " -- Done")
        sleep(5)




# if __name__ == '__main__':
#     link = 'https://www.chemistwarehouse.com.au/buy/65966'
#         # link = 'https://www.chemistwarehouse.com.au/buy/65967'
#     update_price(get_list());