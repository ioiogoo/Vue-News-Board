# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2017/1/3 14:36
'''
from bs4 import BeautifulSoup
import lxml
import requests
from models import sql

from spider import Base

class Hacker_news(Base):
    def __init__(self):
        super(Hacker_news, self).__init__()
        self.name = 'Hacker_news'
        self.url = 'https://news.ycombinator.com/newest'

    def parse_and_save(self):
        pass

    def parse(self):
        try:
            html = requests.get(self.url, headers=self.headers).content
            soup = BeautifulSoup(html, 'lxml')
            news = []
            for story in soup.find_all(class_="storylink"):
                news.append(dict(title=story.get_text(), url=story['href']))
            status = 0
            return status, news
        except Exception as e:
            return 1, e


if __name__ == '__main__':
    h = Hacker_news()
    h.parse()
