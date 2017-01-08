# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2017/1/3 14:36
'''
from bs4 import BeautifulSoup

import requests

from base import Base
from models import Hacker_news
from peewee import IntegrityError


class Hacker_new(Base):
    def __init__(self):
        super(Hacker_new, self).__init__()
        self.name = 'Hacker_news'
        self.url = 'https://news.ycombinator.com/newest'

    def handle(self):
        status, results = self.parse()
        if not status:
            for new in results[::-1]:
                try:
                    Hacker_news(title=new['title'], url=new['url'], intro=new['intro']).save()
                except IntegrityError:
                    pass
	    print '%s is done...' % self.name

        else:
            print results

    def parse(self):
        try:
            print '%s is parse......' % self.name
            html = requests.get(self.url, headers=self.headers).content
            soup = BeautifulSoup(html, 'lxml')
            news = []
            for story in soup.find_all(class_="storylink"):
                news.append(dict(title=story.get_text(), url=story['href']))
            status = 0
            # subtext = soup.find_all(class_="subtext")
            for intro, new in zip(soup.find_all(class_="subtext"), news):
                new['intro'] = intro.get_text()
            # for index in range(len(news)):
            #     news[index]['intro'] = subtext[index].get_text()
            return status, news
        except Exception as e:
            return 1, e


if __name__ == '__main__':
    h = Hacker_new()
    h.handle()
