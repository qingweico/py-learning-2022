from urllib import request
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
url = 'http://httpbin.org/post'
post_data = {
    'k': 'v'
}
data = bytes(parse.urlencode(post_data), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
