import io
import json
import sys
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode("euc-kr")
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#siselist_tab_0 > tr")



for i,e in enumerate(top10):
    if e.find("a") is not None:
        #print(e)
        print("상한가 종목 >>> ",e.select_one(".tltle").string)
