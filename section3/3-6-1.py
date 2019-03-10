import sys
import io
from selenium import webdriver


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



driver = webdriver.PhantomJS('c:/section3/webdriver/phantomjs/phantomjs')

#암묵적으로 5초정도 기다림
driver.implicitly_wait(5)
#google 사이트에 들어가기
driver.get('https://google.com')
#google 사이트의 스크린은 찍어서 저장
driver.save_screenshot("c:/website1.png")


#위의 과정과 동일 --> daum 스크린을 찍기
driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("c:/website2.png")

driver.quit()

print("스크린샷 완료!!")
