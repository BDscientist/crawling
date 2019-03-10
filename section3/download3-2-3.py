import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


s= requests.Session()


r= s.get('http://httpbin.org/stream/20', stream=True)
#print(r.text)
#print(r.encoding) #인코딩이 어떤것으로 되어있는지 확인
#print(r.json()) #json인가 확인하는 코딩문

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b =json.loads(line) #dict 임
    for e in b.keys():
        print("key:",e,"values:",b[e])
