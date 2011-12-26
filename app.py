import os

# import flask
from flask import Flask, make_response, request

# import pygments
from pygments import highlight
from pygments.lexers import (get_lexer_by_name, get_lexer_for_filename,
                             get_lexer_for_mimetype, guess_lexer_for_filename,
                             guess_lexer)
from pygments.formatters import get_formatter_by_name

# initialize flask
app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api')
def api_root():
    resp = make_response('{"version": "0.0.1"}', 200)
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/api/highlight', methods = ['POST'])
def api_highlight():
    if 'source' not in request.json:
        return make_response(None, 422)

    if 'lang' in request.json:
        lexer = get_lexer_by_name(request.json['lang'])
    elif 'filename' in request.json:
        lexer = guess_lexer_for_filename(request.json['filename'],
                                         request.json['source'])
    elif 'mimetype' in request.json:
        lexer = get_lexer_for_mimetype(request.json['mimetype'])
    else:
        lexer = guess_lexer(request.json['source'])

    formatter = get_formatter_by_name('html')
    return highlight(request.json['source'], lexer, formatter)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
