from flask import (
    Flask,
    Response,
    redirect,
    url_for,
)

from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mobilefoodalerts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database 
db = SQLAlchemy(app)

# Models
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    cellphone_number = db.Column('cellphone_number', db.String(120), nullable=False)
    zip_code = db.Column('zip_code', db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.cellphone_number)
    
@app.route('/', methods=['GET'])
def index():
    print('Hello, World!')
    return Response('test', status=200, mimetype='text/html')