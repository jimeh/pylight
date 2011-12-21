import os
from flask import Flask
from flask import make_response
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api')
def api_root():
    resp = make_response('{"version": "0.0.1"}', 200)
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/post', methods = ['POST'])
def post_me():
    return request.json['stuff']


if __name__ == '__main__':
    app.run()
