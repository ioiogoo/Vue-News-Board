# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-7 下午2:06
'''
import requests
from base import Base
from models import Bobao_news
import json
from peewee import IntegrityError


class Bobao_new(Base):
    def __init__(self):
        super(Bobao_new, self).__init__()
        self.name = 'Bobao_news'
        self.url = 'https://api.anquanke.com/data/v1/posts'

    def parse(self):
        try:
            print '%s is parse......' % self.name
            news = []
            for page in range(1,3):
                html = requests.get(url=self.url, headers=self.headers, data={'page': page, 'size': 10, 'sticky': "true"}).content
                html = json.loads(html)
                for data in html['data']:
                    news.append(dict(title=data['title'], url=data['url'], time=data['date'], intro=data['desc']))
            return 0, news
        except Exception as e:
            return 1, e

    def handle(self):
        status, news = self.parse()
        if not status:
            for new in news[::-1]:
                try:
                    Bobao_news(title=new['title'],
                             url=new['url'],
                             time=new['time'],
                             intro=new['intro']).save()
                except IntegrityError:
                    pass
	    print '%s is done...' % self.name

        else:
            print news

if __name__ == '__main__':
    b = Bobao_new()
    b.handle()
