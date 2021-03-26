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

# Helper Table
users_has_service_types = db.Table('users_has_service_types',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('service_types_id', db.Integer, db.ForeignKey('service_types.id'), primary_key=True)
)

# Models
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    cellphone_number = db.Column('cellphone_number', db.String(120), nullable=False, unique=True)
    zip_code = db.Column('zip_code', db.Integer, nullable=False)
    users_has_service_types = db.relationship('Service_Types', secondary=users_has_service_types, lazy='subquery', backref=db.backref('users', lazy=True))
    def __repr__(self):
        return '<User {}>'.format(self.cellphone_number)

class Providers(db.Model):
    __tablename__ = 'providers'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(120))
    address = db.Column('address', db.String(255), nullable=False)
    description = db.Column('description', db.String(255))
    website = db.Column('website', db.String(255))
    service_types_id = db.Column(db.Integer, db.ForeignKey('service_types.id'), nullable=False)
    events = db.relationship('Events', backref='provider', lazy=True)

    def __repr__(self):
        return '<Provider{}>'.format(self.name)

class Service_types(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    service_type = db.Column('type', db.String(64), nullable=False)
    providers = db.relationship('Providers', backref='service_type', lazy=True)

    def __repr__(self):
        return '<Service Type{}>'.format(self.service_type)

class Events(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    start_datetime = db.Column('start_datetime', db.DateTime, nullable=False)
    end_datetime = db.Column('end_datetime', db.DateTime, nullable=False)
    providers_id = db.Column(db.Integer, db.ForeignKey('providers.id'), nullable=False)
    def __repr__(self):
        return '<Event{}>'.format(self.id)

# Routes
@app.route('/', methods=['GET'])
def index():
    print(test)
    return Response('test', status=200, mimetype='text/html')