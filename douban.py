# -*- coding: utf-8 -*-
import json
from lxml import etree
import requests
import time


def get_one_page(url, headers):
    try:
        time.sleep(0.2)
        response = requests.get(url=url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response
        return None
    except TimeoutError:
        print("Time Out", url)
        time.sleep(1)
        return get_one_page(url=url, headers=headers)
    except Exception as e:
        print(e, url)
        time.sleep(1)
        return get_one_page(url=url, headers=headers)

def parse(html):
    ele = etree.HTML(html)
    for book in ele.xpath('//div[@class="indent"]//table//tr'):
        item = {
            "book_name": book.xpath('./td[2]/div/a/@title')[0],
            "book_url": book.xpath('./td[2]/div/a/@href')[0],
            "book_info": book.xpath('./td[2]/p[1]/text()')[0],
            "book_comments_num": book.xpath('./td[2]/div[2]/span[3]/text()')[0].replace("(", "").replace(")", "").strip(),
            "book_star": book.xpath('./td[2]/div[2]/span[2]/text()')[0],
            "book_overview": book.xpath('./td[2]/p[2]/span/text()')[0] if len(book.xpath('./td[2]/p[2]/span/text()')) else None
        }
        yield item

def save(item):
    with open("douban_book_top250", "a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False))
        f.write("\n")

def run():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    }
    for page in range(10):
        url = "https://book.douban.com/top250?start={}".format(page * 25)
        html = get_one_page(url=url, headers=headers).text
        for item in parse(html):
            save(item=item)

if __name__ == '__main__':
    s = time.time()
    run()
    e = time.time()
    print(e-s)
