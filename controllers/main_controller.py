from flask import Blueprint, render_template, jsonify
from extensions import db
from sqlalchemy import text
from flask_login import login_required
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@main.route('/train_info')
def train_info():
    return render_template('train_info.html')

@main.route('/coach_info')
def coach_info():
    return render_template('coach_info.html')

@main.route('/seat_info')
def seat_info():
    return render_template('seat_info.html')

@main.route('/book_seat_info')
def book_seat_info():
    return render_template('book_seat_info')

@main.route('/payment')
def payment():
    return render_template('payment.html')

@main.route('/seating_summary')
def seating_summary():
    return render_template('seating_summary.html')

@main.route('/payment_success')
def payment_success():
    return render_template('payment_success.html')

@main.route('/booking_list')
def booking_list():
    return render_template('booking_list.html')

@main.route('/login_test')
def login_test():
    return render_template('login_test.html')

@main.route('/test_connection')
def test_connection():
    try:
        db.session.execute(text('SELECT 1'))
        return 'Database connection is working!', 200
    except Exception as e:
        return f'Error connecting to the database: {e}', 500