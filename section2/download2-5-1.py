from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(">>",urljoin(baseUrl,"b.html")) # test.com까지만 정해주고 그 뒤에 b.html이 붙음
print(">>",urljoin(baseUrl,"sub/b.html"))
print(">>",urljoin(baseUrl,"../index.html"))
print(">>",urljoin(baseUrl,"../img/img.jpg"))
print(">>",urljoin(baseUrl,"../css/omg.css"))
