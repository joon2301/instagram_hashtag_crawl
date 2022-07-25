from login import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

SCROLL_PAUSE_TIME = 1.5
link_collection = []

def hashtag_search(word):
    url = "https://www.instagram.com/explore/tags/{}/".format(word)
    driver.get(url)
    sleep(5)

def url_list(word):
    hashtag_search(word)
    pageString = driver.page_source
    bs = BeautifulSoup(pageString, 'lxml')
    for link1 in bs.find_all(name = 'div', attrs={'class':'_ac7v _aang'}):
        try: 
            title = link1.select('a')[0] 
            link = title.attrs['href']
            link_collection.append(link)
            title = link1.select('a')[1]
            link = title.attrs['href']
            link_collection.append(link)
            title = link1.select('a')[2]
            link = title.attrs['href']
            link_collection.append(link)
        except:
            break
            if len(link_collection) > 8:
                break

    print(link_collection)
    return link_collection

