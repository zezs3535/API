from selenium import webdriver
import time
import requests
import schedule
from bs4 import BeautifulSoup

member_num=input('아이디 입력 : ')
pw=input('비밀번호 : ')
driver=webdriver.Chrome('url')

driver.implicitly_wait(4)
driver.get('https://www.musinsa.com/?mod=login&referer=https%3A%2F%2Fwww.musinsa.com%2Findex.php%3F')
time.sleep(0.5)
driver.execute_script("document.getElementsByName('id')[0].value=\'" + member + "\'")
time.sleep(0.5)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_css_selector('span.submit').click()
driver.implicitly_wait(3)
time.sleep(0.5)
driver.close()
