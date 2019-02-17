from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath ="C:\\imagedown3\\"
base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")

url = base + quote

res = req.urlopen(url).read()

soup = BeautifulSoup(res,"html.parser")

recommand = soup.select("ul.slides")[2]
#print(recommand)
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


for i,e in enumerate(recommand,1):
    # open앞 파일 경로 + "파일의 이름", "어떠한 형식으로 작성할것인지"
    with open(savePath+"title_"+str(i)+".txt", "wt") as f:
        f.write(e.select_one("h4.block_title > a ").string)
    fullfilename = os.path.join(savePath, savePath+'img_'+str(i)+'.png')
    #urlretrieve 기능은 앞에 파일원본, 파일이 들어갈 경로
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)

print("강좌 정보 텍스트 출력 및 이미지 다운 완료!")
