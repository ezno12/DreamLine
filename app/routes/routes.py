"""modul contain all route"""
from flask import Flask, render_template
from app.app import app
from models import User,RegisterForm

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')