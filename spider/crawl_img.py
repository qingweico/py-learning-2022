from bs4 import BeautifulSoup
import requests
import os
import shutil

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
url = 'https://sc.chinaz.com/tupian/'


# 下载图片
def download_img(image_url, image_local_path):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_local_path, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)


def crawl(site_url):
    response = requests.get(site_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for pic_href in soup.find_all('div', class_=''):
        for pic in pic_href.find_all('img'):
            img_url = pic.get('src')
            dir_path = os.path.abspath('pic')
            filename = os.path.basename(img_url)
            img_path = os.path.join(dir_path, filename)
            print('开始下载 %s' % img_url)
            download_img(img_url, img_path)


crawl(url)
