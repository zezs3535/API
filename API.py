# # API 사용해보기
# import requests as rq
# import xml.etree.ElementTree as ET
# from bs4 import BeautifulSoup as bs
# url = "http://www.chungbuk.go.kr/openapi-data/service/priceinfo/priceinfo"

# res = rq.get(url)
# xmlRowdata=res.content.decode('utf-8')
# soup=bs(xmlRowdata,'html.parser')

# for i in soup.find_all('price'):
#     print(i)

# print(res.status_code)
# if res.status_code==200:
#     print("요청 성공")
# else:
#     print("에러")

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import time

if __name__ == "__main__":
    keyword = input("검색할 키워드를 입력하세요 : ")

    url = requests.get(
        "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%s" % keyword)

    soup = BeautifulSoup(url.text, 'html.parser')
    title = soup.select('.news .type01 li dt a')
    uploadTime = soup.select('.news .type01 li dd span')
    f = open("News.txt", "w")
    for i in title:
        f.write(i.attrs['title'])
        f.write("\nURL : ")
        f.write(i.attrs['href'])
        f.write("\n")
        f.write("\n")
    f.close()
