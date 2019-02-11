import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "http://cafefiles.naver.net/20150404_41/onehodang2_1428121325007MWF8c_JPEG/10.jpg"
htmlURL = "http://google.com"

savePath1 = "C:/section2/test1.jpg"
savePath2 = "C:/section2/index.html"

f = dw.urlopen(imgUrl).read()
saveFile1 = open(savePath1,'wb') # w : write, r : read, a:add
saveFile1.write(f)
saveFile1.close() # 무조건 해봐야함 리소스 복귀함. 메모리낭비 ㄴㄴ!


#위의 구문보다  더 좋음 왜냐하면 리소스를 자동적으로 반납하는 기능이 있음.
f2 = dw.urlopen(htmlURL).read()
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)




print("파이썬 버전")
print("다운로드 완료")
