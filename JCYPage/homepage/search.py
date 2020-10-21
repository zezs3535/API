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
    data={}
    for i in title:
        data[i.title]=title.get('href')
    #f = open("News.txt", "w")
    # for i in title:
    #     f.write(i.attrs['title'])
    #     f.write("\nURL : ")
    #     f.write(i.attrs['href'])
    #     f.write("\n")
    #     f.write("\n")
    # f.close()
