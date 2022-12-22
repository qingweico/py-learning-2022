from bs4 import BeautifulSoup
# pip install lxml
# pip install bs4
import requests

url = 'http://qingweico.cn'
content = requests.get(url).text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.p)
