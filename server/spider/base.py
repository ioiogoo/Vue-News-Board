# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 17-1-6 下午10:24
'''

class Base(object):
    def __init__(self):
        self.news_count = 20
        self.name = ''
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }


    def parse(self):
        pass

    def handle(self):
        pass