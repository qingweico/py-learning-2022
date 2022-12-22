import requests
import re

url = 'http://www.cnu.cc/discoveryPage/hot-0'
content = requests.get(url).text
pattern = re.compile(r'<a href="(.*?)".*?title.*?author">(.*?)</div>', re.S)
results = re.findall(pattern, content)

# TODO
for result in results:
    url, title = result
    print(url, re.sub('\\s', '', title))
