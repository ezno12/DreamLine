
"""
modul contain User database
"""
from app.app import *


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    first_name = db.Column(db.String(15), nullable = False)
    last_name = db.Column(db.String(15), nullable = False)
    password_hash = db.Column(db.String(length=30), nullable=False)
