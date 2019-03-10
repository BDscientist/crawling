import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


s= requests.Session()
r= s.get('http://httpbin.org/get')
#print(r.status_code)
#print(r.ok)

#http://jsonplaceholder.typicode.com

r= s.get('http://jsonplaceholder.typicode.com/albums/1')
#print(r.text) #array 형태로 가져옴
print(r.json())
print(r.json().keys())
print(r.json().values())
print(r.encoding )
print(r.content)
print(r.raw)
