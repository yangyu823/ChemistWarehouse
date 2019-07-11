#!/usr/bin/python

import os
import requests
from lxml import html
from time import sleep
import mysql.connector
import json
from backend.Price_get.get_data import check_data
from datetime import datetime
from selenium import webdriver

# from backend.Price_get.fuc_agent import get_agent

# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

connection = mysql.connector.connect(host='localhost',
                                     port='8889',
                                     database='price_db',
                                     user='root',
                                     password='root')


def get_list():
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
    return url_list


if __name__ == '__main__':
    # link = 'https://www.chemistwarehouse.com.au/buy/65966'
    #     # link = 'https://www.chemistwarehouse.com.au/buy/65967'
    print(get_list())
