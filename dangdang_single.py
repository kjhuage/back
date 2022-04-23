import requests
from bs4 import BeautifulSoup
import time

class DangDang():
    def get_data(url,header):
        res = requests.get(url, headers=header)
        soup = BeautifulSoup(res.text, 'html.parser')
        titles = soup.select('li > p.name > span.search_now_price')
        price = soup.select('li > p.price > span.search_now_price')
        authors = soup.select('li > p.search_book_author > span > a')
        publishs = soup.select('li > p.search_book_author > span:nth-of-type(3) > a ')
        for x in titles:
            print(x.get_text()[0:])
        for x in price:
            print(x.get_text()[1:])
        for x in authors:
            print(x.get_text()[0:])
        for x in publishs:
            print(x.get_text()[0:])

    if __name__ == 'main':
        header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        url = 'http://search.dangdang.com/?key=Python&act=input&page_index=1'
        get_data(url)
        time.sleep(3)
        print(url)


