from flask import (
    Flask,
    Response,
    redirect,
    url_for,
)
import datetime
from flask_sqlalchemy import SQLAlchemy
from data import test, mock_users_data, providers_data, service_types_data

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
    users_has_service_types = db.relationship('Service_types', secondary=users_has_service_types, lazy='subquery', backref=db.backref('users', lazy=True))
    def __repr__(self):
        return '<User {}>'.format(self.cellphone_number)

class Providers(db.Model):
    __tablename__ = 'providers'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(120))
    address = db.Column('address', db.String(255), nullable=False)
    description = db.Column('description', db.String(255))
    website = db.Column('website', db.String(255))
    service_types_id = db.Column(db.Integer, db.ForeignKey('service_types.id'))
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

# #Add data to database from data.py (only need to do this once to generate the db.content)
# for user in mock_users_data:
#     print(user)
#     user_data = Users(
#         id=user['id'],
#         cellphone_number=user['cellphone_number'],
#         zip_code=user['zip_code']
#     )
#     db.session.add(user_data)
#     print('All Users',Users.query.all())

# for service in service_types_data:
#     print(service)
#     service_data = Service_types(
#         id=service['id'],
#         service_type=service['service_type']
#     )
#     db.session.add(service_data)
#     print('All Service Types', Service_types.query.all())

# for provider in providers_data:
#     print(provider['name'], provider['service_type_id'])
#     # Get service_type based on service_type_id
#     service_type = Service_types().query.filter_by(id=provider['service_type_id']).first()
#     print('Query service type id', service_type, service_type.id)

#     provider_data = Providers(
#         id=provider['id'],
#         name=provider['name'],
#         address=provider['address'],
#         description=provider['description'],
#         website=provider['website'],
#         service_types_id=service_type.id
#     )
   
#     db.session.add(provider_data)
#     print('All Providers', Providers.query.all())

# #Commit all data to db
# db.session.commit()

# Confirm all starter data is in database
print('All Users', Users.query.all())
print('All Providers', Providers.query.all())
print('All Service Types', Service_types.query.all())
# Routes
@app.route('/', methods=['GET'])
def index():
    print(test)
    return Response('test', status=200, mimetype='text/html')
