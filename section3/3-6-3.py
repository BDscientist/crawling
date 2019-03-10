import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless") #  구글 웹을 보면서 개발하지 않고 내부적으로 코드를 처리하는 방법 : CLI
firefox_options.add_argument('--log-level=3')


driver = webdriver.Firefox(executable_path='C:/section3/webdriver/firefox/geckodriver')

#driver.set_window_size(1920, 1280)
#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot("c:/picture/a_firefox.png")



#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot("c:/picture/b_firefox.png")

driver.quit()

print("스크린샷 완료!!")
