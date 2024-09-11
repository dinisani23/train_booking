from flask import Blueprint, request, session, redirect, url_for, flash, jsonify, render_template
from werkzeug.security import check_password_hash
from models import Booking, Schedule, Seat
from extensions import db
from flask_login import current_user
import sys
from sqlalchemy.orm import Session
from sqlalchemy import update
import datetime

confirm_tix = Blueprint('book_seat_confirm', __name__)

@confirm_tix.route('/book_seats_confirm/<booking_id>/<booked_train>', methods=['GET', 'POST'])
def book_seats_confirm(booking_id, booked_train):
    if current_user.is_authenticated:
        booking = Booking.query.filter_by(
            id=booking_id
        ).first()

        if booking:
            booking.seat_status = 1
            db.session.commit()
        else:
            return "Error confirming your seat1"
        
        #return str(booking.seat_number)

        seat = Seat.query.filter_by(
                #id=booking.train_number
                train_number=booked_train,
                coach_number=booking.coach_number,
                seat_number=booking.seat_number
            ).first()

        if seat:
            seat.seat_status = 0
            seat.locked_until = datetime.datetime.now() + datetime.timedelta(minutes=10)
            db.session.commit()
            #return str(datetime.datetime.now() + datetime.timedelta(minutes=10)) #payment
            tix = Schedule.query.filter_by(
                id=booking.train_number
            ).first()
            #return "seccess"
            confirmed_seat_detail = [
                {
                    'id': tix.id,
                    'train_number': tix.train_number,
                    'origin': tix.origin,
                    'destination': tix.destination,
                    'date': tix.departure_date.isoformat(),
                    'departure_time': tix.departure_time.strftime('%H:%M'),
                    'arrival_time': tix.arrival_time.strftime('%H:%M'),
                    'departure_date': tix.departure_date.isoformat(),
                    'price': tix.price,
                    'coach_number': booking.coach_number,
                    'seat_number': booking.seat_number
                }
            ]
            jsonify({
                'confirmed_seat_detail': confirmed_seat_detail
            })
            return render_template('payment.html', booking_id=booking.id, confirmed_summary=confirmed_seat_detail)
        else:
            return "Error confirming your seat2"
        
        
        #seat.locked_until = datetime.datetime.now() + datetime.timedelta(minutes=10)
    else:
        return "Error: not logged in"

