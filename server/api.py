# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-7 下午2:50
'''
from flask_restful import Resource, reqparse
from server.spider.models import *

model_map = {
    'hacker': Hacker_news,
    'freebuf': Freebuf_news,
    'jobbole': Jobbole_news,
    'bole': Bobao_news
}

class getNews(Resource):
    def __init__(self):
        super(getNews, self).__init__()
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('cat', type=unicode, required=True, location='args')

    def get(self):
        model = self.parse.parse_args().get(u'cat').encode('utf-8')
        model = model_map[model]
        status, data = self.select(model)
        print data
        return {'status': status, 'data': data}


    def select(self, model):
        news = []
        try:
            for new in model.select().order_by(model.id.desc()).limit(20):
                news.append(dict(title=new.title,
                             url=new.url,
                             intro=new.intro,
                             time=new.time))
            return 0, news
        except Exception as e:
            return 1, e







