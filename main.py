from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from login import LoginInstagram,driver
from urlCrawl import url_list
from dataCrawl import data

import requests
import json
# 로그인 정보
LoginInstagram('','')
sleep(3)
# 해시태그 검색
crawlURL = url_list('')
crawlData = data(crawlURL)

print(len(crawlData))
print(crawlData)

sleep(3)
