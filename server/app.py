#! /bin/bash
from flask import Flask, render_template, request, current_app
from flask_restful import Api
from api import getNews, log, updateNews
from config import *
from logger import logger

app = Flask(__name__)
api = Api(app)


@app.route('/')
@log
def hello_world():
    return render_template('index.html')


api.add_resource(getNews, '/api/getNews')
api.add_resource(updateNews, '/api/updateNews')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
