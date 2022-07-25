from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


driver = webdriver.Chrome('C:/Users/admin/Desktop/HashtagCrawl/chromedriver.exe')

def LoginInstagram(strId, strPassword) :
        driver.get('https://www.instagram.com')
        sleep(3) #웹 페이지 로드를 보장하기 위해 3초 쉬기
        id_input = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(1) > div > label > input')
        id_input.send_keys(strId)
        password_input = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(2) > div > label > input')
        password_input.send_keys(strPassword)
        password_input.submit()
        sleep(3)