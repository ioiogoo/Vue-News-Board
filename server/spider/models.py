# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2017/1/3 15:11
'''
from peewee import *
import os

path = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(path, 'news.db')
db = SqliteDatabase(db_path)


class Hacker_news(Model):
    title = CharField(unique=True)
    url = CharField(unique=True)
    time = CharField(null=True)
    intro = CharField(null=True)

    class Meta:
        database = db

class Freebuf_news(Model):
    title = CharField(unique=True)
    url = CharField(unique=True)
    time = CharField(null=False)
    intro = CharField(null=False)

    class Meta:
        database = db

class Jobbole_news(Model):
    title = CharField(unique=True)
    url = CharField(unique=True)
    time = CharField(null=False)
    intro = CharField(null=False)

    class Meta:
        database = db

class Bobao_news(Model):
    title = CharField(unique=True)
    url = CharField(unique=True)
    time = CharField(null=False)
    intro = CharField(null=False)

    class Meta:
        database = db


def create_table(model):
    if not model.table_exists():
        model.create_table()

models = [Hacker_news, Freebuf_news, Jobbole_news, Bobao_news]
if __name__ == '__main__':
    db.connect()
    for model in models:
        create_table(model)

