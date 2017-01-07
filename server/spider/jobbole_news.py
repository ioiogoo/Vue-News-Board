# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-7 下午1:31
'''
from bs4 import BeautifulSoup
import requests
from base import Base
from server.spider.models import Jobbole_news
from peewee import IntegrityError


class Jobbole_new(Base):
    def __init__(self):
        super(Jobbole_new, self).__init__()
        self.name = 'Jobbole_news'
        self.url = 'http://blog.jobbole.com/all-posts/'

    def parse(self):
        try:
            print '%s is parse......' % self.name
            html = requests.get(url=self.url, headers=self.headers).content
            soup = BeautifulSoup(html, 'lxml')
            news = []
            for new in soup.find_all(class_="post floated-thumb"):
                title = new.find('p').a['title']
                url = new.find('p').a['href']
                time = new.find('p').get_text('////').split('////')[-3].replace(u'·', '').strip()
                intro = new.find(class_="excerpt").get_text().strip()
                news.append(dict(title=title, url=url, time=time, intro=intro))
            return 0, news
        except Exception as e:
            return 1, e

    def handle(self):
        status, news = self.parse()
        if not status:
            for new in news:
                try:
                    Jobbole_news(title=new['title'],
                             url=new['url'],
                             time=new['time'],
                             intro=new['intro']).save()
                except IntegrityError:
                    pass
        else:
            print news

if __name__ == '__main__':
    j = Jobbole_new()
    j.handle()
