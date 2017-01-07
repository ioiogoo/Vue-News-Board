# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-7 下午12:52
'''
from bs4 import BeautifulSoup

import requests

from base import Base
from server.spider.models import Freebuf_news
from peewee import IntegrityError


class Freebuf_new(Base):
    def __init__(self):
        super(Freebuf_new, self).__init__()
        self.name = 'Freebuf_news'
        self.url = 'http://www.freebuf.com/page/%d'

    def parse(self):
        try:
            print '%s is parse......' % self.name
            for page in range(1, 4):
                html = requests.get(url=self.url % page, headers=self.headers).content
                soup = BeautifulSoup(html, 'lxml')
                news = []
                for new in soup.find_all(class_="news-info"):
                    title = new.find('dt').a['title'].strip()
                    url = new.find('dt').a['href']
                    time = new.find(class_="time").get_text().strip()
                    intro = new.find(class_="text").get_text().strip()
                    news.append(dict(title=title, url=url,time=time,intro=intro))

            return 0, news
        except Exception as e:
            return 1, e

    def handle(self):
        status, news = self.parse()
        if not status:
            for new in news:
                try:
                    Freebuf_news(title=new['title'],
                             url=new['url'],
                             time=new['time'],
                             intro=new['intro']).save()
                except IntegrityError:
                    pass
        else:
            print news

if __name__ == '__main__':
    f = Freebuf_new()
    f.handle()
