from flask import (
    Flask,
    Response,
    redirect,
    url_for,
)
import datetime
from flask_sqlalchemy import SQLAlchemy
from data import test

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
    cellphone_number = db.Column('cellphone_number', db.String(120), nullable=False, unique=True)
    zip_code = db.Column('zip_code', db.Integer, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.cellphone_number)

class Providers(db.Model):
    __tablename__ = 'providers'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(120))
    address = db.Column('address', db.String(255), nullable=False)
    description = db.Column('description', db.String(255))
    website = db.Column('website', db.String(255))

    def __repr__(self):
        return '<Provider{}>'.format(self.name)

class Service_Types(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    service_type = db.Column('type', db.String(64), nullable=False)

    def __repr__(self):
        return '<Service Type{}>'.format(self.service_type)

class Events(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    start_datetime = db.Column('start_datetime', db.DateTime, nullable=False)
    end_datetime = db.Column('end_datetime', db.DateTime, nullable=False)

    def __repr__(self):
        return '<Event{}>'.format(self.id)

# Routes
@app.route('/', methods=['GET'])
def index():
    print(test)
    return Response('test', status=200, mimetype='text/html')