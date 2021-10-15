"""
modul contain form for user registeration
"""
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from app.app import db

class RegisterForm(FlaskForm):
    username = StringField(label='User Name:')
    first_name = StringField(label='User Name:')
    last_name = StringField(label='User Name:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')
