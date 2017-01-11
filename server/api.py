#! /usr/bin/bash
# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-7 下午2:50
'''
from flask_restful import Resource, reqparse, request
from flask import current_app
from spider.models import *
from functools import wraps
from logger import logger
from spider.manage import crawl
import time

model_map = {
    'hacker': Hacker_news,
    'freebuf': Freebuf_news,
    'jobbole': Jobbole_news,
    'bobao': Bobao_news
}

def log(func):
    @wraps(func)
    def wrapper(*arg, **kwarg):
        if request.headers.get('X-Forwarded-For'):
            logger.info('%s is done, ip: %s' % (func.__name__, request.headers.get('X-Forwarded-For')))
        else:
            logger.info('%s is done, ip: %s' % (func.__name__, request.remote_addr))
        return func(*arg, **kwarg)
    return wrapper



class getNews(Resource):
    def __init__(self):
        super(getNews, self).__init__()
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('cat', type=unicode, required=True, location='args')
        self.parse.add_argument('jsonp', type=unicode, required=False, location='args')
    @log
    def get(self):
        model = self.parse.parse_args().get(u'cat').encode('utf-8')
        model = model_map.get(model, None)
        if not model:
            return {'status': 1, 'data': None}, 400
        status, data = self.select(model)
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

class updateNews(Resource):
    @log
    def post(self):
        try:
            lasttime = getattr(current_app, 'lasttime', None)
            if lasttime and time.time() - lasttime > 600 or not lasttime:
                current_app.lasttime = time.time()
                crawl()
                logger.info('updateNews is done')
            else:
                logger.info('updateNews is done, but not crawl')
            return {'status': 0, 'data': None}
        except Exception as e:
            logger.error('updateNews is wrong,error: %s' % e)
            return {'status': 1, 'data': None}, 500








