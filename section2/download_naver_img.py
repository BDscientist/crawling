import io
import json
import sys
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as rep
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base +quote
#print(url)

res = req.urlopen(url)
savePath = "C:\\imagedown\\" #c:/imagedown


try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno !=errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res,"html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img ")
print("test >> ",img_list)



for i ,img_list in enumerate(img_list,1):
    #print(img_list['data-source'])
    fullFileName = os.path.join(savePath,savePath+str(i)+'jpg')
    req.urlretrieve(img_list['data-source'],fullFileName)

print("다운로드완료!")
