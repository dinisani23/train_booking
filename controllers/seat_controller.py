from flask import Blueprint, request, session, redirect, url_for, flash, jsonify, render_template
from werkzeug.security import check_password_hash
from models import Booking, Schedule, Seat
from extensions import db
from flask_login import current_user
import sys
from sqlalchemy.orm import Session
from sqlalchemy import update
import datetime

seat = Blueprint('seat_info', __name__)

@seat.route('/seats/<booking_id>/<coach_number>', methods=['GET', 'POST'])
def seats(booking_id, coach_number):
    if current_user.is_authenticated:

        booking = Booking.query.filter_by(
            id=booking_id
        ).first()

        #booking = db_session.query(Booking).filter(Booking.email == current_user_email).first()

        if booking:
            booking.coach_number = coach_number
            db.session.commit()
        else:
            return "Error booking your coach"
        
        tix = Schedule.query.filter_by(
                id=booking.train_number
            ).first()
        seat_all = Seat.query.filter_by(
                train_number=tix.train_number,
                coach_number=coach_number
            ).all()
        
        #if seat_all.locked_until > datetime.datetime.now()
        current_timestamp = datetime.datetime.now()
        
        seat_list = [
                {
                    'id': seats.id,
                    'train_number': seats.train_number,
                    'coach_number': seats.coach_number,
                    'seat_number': seats.seat_number,
                    'seat_status': seats.seat_status,
                    'locked_until': seats.locked_until
                }
                for seats in seat_all
            ]
        
        jsonify({
                'seat_list': seat_list
            })
        
        flash('Booking created successfully with coachnumber!')
        return render_template('seat_info.html', booking_id=booking.id, seat_available=seat_list, current_timestamp=current_timestamp)
        #redirect(url_for('main.coach_info', coach_available=coach_list))
    else:
        return "Error: not logged in"

    