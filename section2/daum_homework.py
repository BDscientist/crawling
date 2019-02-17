from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
#print(soup)

#daum_is = soup.select("div.realtime_part > ol.list_hotissue.issue_row >sapn.txt_issue > a ")
daum_is = soup.find_all("a",tabindex="-1")
print(daum_is)
#print(daum_is)

for i,e in enumerate(daum_is,1):
    print(i,e.string)
