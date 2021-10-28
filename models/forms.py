"""
modul contain form for user registeration
"""
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from app.app import db
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from models.user import User


class RegisterForm(FlaskForm):
    """
    class for register new user
    """
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    
    def validate_full_name(self, full_name_to_check):
        full_name = User.query.filter_by(full_name=full_name_to_check.data).first()
        
        if full_name:
            raise ValidationError('Name already exists!')

    username = StringField( validators=[Length(min=2, max=30), DataRequired()])
    full_name = StringField(validators=[Length(min=2, max=40), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    """
    Class login form for existing user
    """
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class DreamsForm(FlaskForm):
    """
    """
    dream1 = StringField()
    dream2 = StringField()
    dream3 = StringField()

class Having(DreamsForm):
    """"""
    havingDream1 = DreamsForm.dream1
    havingDream2 = DreamsForm.dream2
    havingDream3 = DreamsForm.dream3

class Being(DreamsForm):
    """"""
    beingDream1 = DreamsForm.dream1
    beingDream2 = DreamsForm.dream2
    beingDream3 = DreamsForm.dream3

class Doing(DreamsForm):
    """"""
    doingDream1 = DreamsForm.dream1
    doingDream2 = DreamsForm.dream2
    doingDream3 = DreamsForm.dream3
