from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from models import User
from flask_login import login_user as flask_login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_login import login_user, logout_user, current_user
from extensions import db

import sys

login = Blueprint('login', __name__)

#class LoginForm(FlaskForm):
    #email = StringField('Email', validators=[DataRequired(), Email()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #submit = SubmitField('Login')

@login.route('/login_buyer', methods=['GET', 'POST'])
def login_buyer():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@login.route('/create_acc', methods=['POST'])
def create_acc():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    repeat_password = request.form.get('repeat_password')
    

    if not email or not password or not repeat_password:
        flash('All fields are required.', 'danger')
        return redirect(url_for('login.create_acc'))
    
        
    if password != repeat_password:
        flash('Passwords do not match.', 'danger')
        return redirect(url_for('login.create_acc'))
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash('Email is already taken.', 'danger')
        return redirect(url_for('main.login'))
        
    hashed_password = generate_password_hash(password)
        
     # Create a new user
    new_user = User(username=name, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return redirect(url_for('main.index'))