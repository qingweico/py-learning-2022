import socket
from urllib import request
from urllib import error
from urllib import parse

print('------------- post -------------')
data = bytes(parse.urlencode({'k': 'v'}), encoding='utf-8')
post_url = 'http://httpbin.org/post'
resp = request.urlopen(post_url, data=data)
print(resp.read().decode('utf-8'))
print('------------- get -------------')
get_url = 'http://httpbin.org/get'
try:
    resp = request.urlopen(get_url, timeout=1)
    print(resp.read().decode('utf-8'))
except error.URLError as ex:
    if isinstance(ex.reason, socket.timeout):
        print('Timeout!')
