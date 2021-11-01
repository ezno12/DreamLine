"""
modul contain application config
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dreamline.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
"""Create Data base"""
db = SQLAlchemy(app)
"""Model Crypt user passwor"""
bcrypt = Bcrypt(app)
"""Manage user session"""
login_manager = LoginManager(app)
