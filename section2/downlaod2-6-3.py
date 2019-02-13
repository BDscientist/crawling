from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


fp = open("cars.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")


def car_func(selector):
    print("car_func >> ",soup.select_one(selector).string)

#람다식
car_lamda = lambda q : print("car_lambda >> ",soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")
print("=================================")
car_lamda("#gr")
car_lamda("li#gr")
car_lamda("ul > li#gr")
car_lamda("#cars #gr")
car_lamda("#cars > #gr")
car_lamda("li[id='gr']")

print("=========================")
print("car_func >> ",soup.select("li")[3].string)
print("car_func >> ",soup.find_all("li")[3].string)
