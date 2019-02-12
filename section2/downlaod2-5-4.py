from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html,'html.parser')

#왜 one을 써주냐면 h1은 lsit이기 때문임 그래서 하나만 가져오려고해도
#for문으로 다 돌려야 함
#ex) [ 1 ]이기 때문에  for로 1을 가져와야함.

h1 = soup.select_one("div#main > h1")
print('h1',h1)
print('h1',h1.string)

# div의 아이디는 : # 로 표현 그리고 main이기 때문에 써주고
#ul태그의 lecs 그리고 li 다가져와라라는 의미!
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>> ",li)
