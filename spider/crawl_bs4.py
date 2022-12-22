import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


# 抓取新闻标题
def crawl_news_title(url):
    rep = requests.get(url, headers=headers)
    soup = BeautifulSoup(rep.text, 'lxml')
    print(soup.find_all('div', class_='inner-content'))


crawl_news_title('https://www.infoq.cn/news')
