from flask import Flask
from flask_restful import Api
from api import getNews

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(getNews, '/api/getNews')

if __name__ == '__main__':
    app.run()
