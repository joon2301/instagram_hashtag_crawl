import csv
from login import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

csvTxt= []

# data lists
instagram_tags = []


def data(urls):
    for i in range(0,len(urls)):
    # for i in range(0,3):
        author = ""
        main_content = ""
        comment_author = []
        comment_context = []
        hashtag=[]
        acctag=[]
        urlcontent = []
        csvTxt.append([])
        print(urls[i])
        try:
            url = 'https://www.instagram.com' + urls[i]
            driver.get(url)
            sleep(3)
            pageString = driver.page_source
            bs = BeautifulSoup(pageString, 'lxml')
        #실패용 예외처리
        except:
            print("링크에러:", i, urls[i])
            continue


        try: #여러개 가져와야하는 것 생각하자
            print("----------------미디어 크롤링--------------------")
            mediacontent = bs.find_all(name='div', attrs={"class":"_ab1c"})
            print(mediacontent[0])
            # 동영상 / 이미지
            try:
                print("동영상: ",mediacontent[0].select('video')[0]['src'])
            except:
                print("이미지: ",mediacontent[0].select('img')[0]['src'])

            print("------------------------------------------------")
        #실패용 예외처리
        except:
            print("미디어 크롤링 에러:", i, urls[i])
            continue

        try:
            print("------------------본문 크롤링--------------------")
            #본문이랑 댓글이 걸러짐 / urlcontent[0]: 본문, data[1:] 댓글
            urlcontent = bs.find_all(name='div', attrs={"class":"_a9zr"})
            # urlcontent[0] 처리 / urlcontent[0][0]: 작성자, urlcontent[0][1]:본문
            author = urlcontent[0].select('span')[0].text
            print("작성자:",author)
            main_content = urlcontent[0].select('span')[1].text
            print("\n본문 전문:",main_content)
            for i in urlcontent[0].select('span a')[1:]:
                if (i.text)[0] == '#':
                    hashtag.append(i.text)
                else:
                    acctag.append(i.text)
            print("\n해시태그 모음:",hashtag)
            print("\n계정태그 모음:",acctag)
            print("------------------------------------------------")
        #실패용 예외처리
        except:
            print("본문 크롤링 에러:", i, urls[i])
            continue

        try:   
            print("------------------날짜 크롤링--------------------")
            datecontent = bs.find_all(name='div', attrs={"class":"_aacl _aacm _aacu _aacy _aad6"})
            print("작성일시: ",datecontent[0].select('time')[0]['datetime'])
            print("------------------------------------------------")
        #실패용 예외처리
        except:
            print("날짜 크롤링 에러:", i, urls[i])
            continue

        try:
            print("------------------댓글 크롤링--------------------")
            # urlcontent[1:] 처리 / urlcontent[1].span[0]: 작성자, urlcontent[1].span[1]:댓글본문
            for data in urlcontent[1:]:
                print("댓글 작성자:",  data.select('span')[0].text)
                print("댓글 본문:",  data.select('span')[1].text)
                print()
                urlcontent.append(data)
            print("------------------------------------------------")
        #실패용 예외처리
        except:
            print("댓글 크롤링 에러:", i, urls[i])
            continue

            # 다음에 해보자
            # 1. csv 저장




        # 디버깅용 lxml 전문 출력
        # print("------------------------------------------------")
        # print(urlcontent[1:])
        # print("------------------------------------------------")

        print("\n\n")
        sleep(5)

    return csvTxt
