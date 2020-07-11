# API 사용해보기
import requests as rq
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
url = "http://www.chungbuk.go.kr/openapi-data/service/priceinfo/priceinfo"

res = rq.get(url)
xmlRowdata=res.content.decode('utf-8')
soup=bs(xmlRowdata,'html.parser')

for i in soup.find_all('price'):
    print(i)
    
    
#print(res.status_code)
# if res.status_code==200:
#     print("요청 성공")
# else:
#     print("에러")
    
# Data=list(res)
# print(type(Data))