import sys
import io
import urllib.request as dw
from urllib.parse import urlencode


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl1 =  "https://ssl.pstatic.net/tveta/libs/1221/1221895/37092d9dcb5ef08d4be4_20190130152106147_5.jpg"
imgUrl2 = "https://ssl.pstatic.net/tveta/libs/1228/1228222/df66026fdfa5786b86a9_20190201114539023.jpg"

savePath1 = "C:/section2/naver1.jpg"
savePath2 = "C:/section2/naver2.jpg"


f1 = dw.urlopen(imgUrl1).read()
with open(savePath1,'wb') as saveFile1:
    saveFile1.write(f1)


#위의 구문보다  더 좋음 왜냐하면 리소스를 자동적으로 반납하는 기능이 있음.
f2 = dw.urlopen(imgUrl2).read()
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)




print("파이썬 버전")
print("다운로드 완료")
