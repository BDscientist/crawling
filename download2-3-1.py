import sys
import io
import urllib.request as req
from urllib.parse import urlparse


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



url ="http://www.encar.com"
mem =req.urlopen(url)

#파이썬 자료형!!!
#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))

#web짤때 알아야할 코드와 정보들!
#print("geturl",mem.geturl())
#print("status",mem.status) #200(정상), 404(없는거), 403, 500(서버오류)
#print("headers",mem.getheaders())
#print("info",mem.info())
#print("code",mem.getcode())
#print("read",mem.read(50))
#print("read",mem.read().decode("utf-8"))
#print("urlpars: ",urlparse("http://www.encar.com?test=test"))
