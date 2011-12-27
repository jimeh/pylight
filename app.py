# import libraries
import os
from flask import *

# import project relative modules
from pylight import *

# initialize flask
app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api')
def api_root():
    return jsonify(version='0.0.1')

@app.route('/api/highlight', methods=['POST'])
def api_highlight():
    response = pylight(request.json)
    if response:
        return jsonify(response)
    else:
        return make_response(None, 422)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    use_debug = os.environ.get('FLASK_ENV', 'development') != 'production'
    app.run(host='0.0.0.0', port=port, debug=use_debug)
