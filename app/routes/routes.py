"""modul contain all route"""
from os import name
from flask import Flask, render_template, url_for, redirect, flash
from app.app import app, db
from models.user import User
from models.dreams import Dreams
from models.forms import RegisterForm, LoginForm, Having, Being, Doing
from flask_login import login_user, logout_user 

@app.route('/')
def home_page():
    """
    redrect to home page
    """
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    """
    sgin up page
    """
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              full_name=form.full_name.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('dreams_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    """
    logout redirect
    """
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/dreams', methods=['GET', 'POST'])
def dreams_page():
    """
    dream page _ contain main page to define dreams.
    """
    having_Dream = Having()
    if having_Dream.validate_on_submit():
        user_having_to_create = Dreams()
        db.session.add(user_having_to_create)
        db.session.commit()


    being_Dream = Being()
    if being_Dream.validate_on_submit():
        user_doing_to_create = Dreams(dream=being_Dream.beingDream1.data)
        db.session.add(user_doing_to_create)
        db.session.commit()


    doing_Dream = Doing()
    if doing_Dream.validate_on_submit():
        user_doing_to_create = Dreams(dream=doing_Dream.doingDream1.data)
        db.session.add(user_doing_to_create)
        db.session.commit()

    return render_template('define_dreams.html', have = having_Dream, be = being_Dream, do = doing_Dream)
