from flask import Flask, render_template
from flask_restful import Api
from api import getNews

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

api.add_resource(getNews, '/api/getNews')

if __name__ == '__main__':
    app.run(debug=False,host='127.0.0.1',port=5002)
