"""
modul contain form for user registeration
"""
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from app.app import db
from wtforms.validators import Length, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField( validators=[Length(min=2, max=30), DataRequired()])
    first_name = StringField(validators=[Length(min=2, max=30), DataRequired()])
    last_name = StringField(validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
