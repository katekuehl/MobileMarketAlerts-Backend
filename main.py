from flask import (
    Flask,
    Response,
    redirect,
    url_for,
)

from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print('Hello, World!')
    return Response('test', status=200, mimetype='text/html')