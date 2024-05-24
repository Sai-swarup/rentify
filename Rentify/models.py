from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(200))
    is_seller = db.Column(db.Boolean)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    area = db.Column(db.String(100))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    nearby = db.Column(db.String(200))
    description = db.Column(db.String(500))
