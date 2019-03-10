import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument("--headless") #  구글 웹을 보면서 개발하지 않고 내부적으로 코드를 처리하는 방법 : CLI
#chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_option= chrome_option,executable_path='c:/section3/webdriver/chrome/chromedriver')

driver = webdriver.Chrome('c:/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
time.sleep(7)
driver.implicitly_wait(5)


driver.find_element_by_name('log').send_keys('vkdvkd3546')
driver.implicitly_wait(1)
driver.find_element_by_name('pwd').send_keys('audgksals12#')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()

print("스크린샷 완료!!")
