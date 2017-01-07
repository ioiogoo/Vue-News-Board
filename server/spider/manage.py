# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-7 下午2:18
'''
from bobao_news import Bobao_new
from freebuf_news import Freebuf_new
from hacker_news import Hacker_new
from jobbole_news import Jobbole_new
from gevent.pool import Pool
from gevent import monkey; monkey.patch_all()
from models import create_table, models

for model in models:
    create_table(model)


news = [Bobao_new, Freebuf_new, Hacker_new, Jobbole_new]
p = Pool()
p.map(lambda x: x().handle(), news)

