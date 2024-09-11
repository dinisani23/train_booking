from flask import Blueprint, request, session, redirect, url_for, flash, jsonify, render_template
from werkzeug.security import check_password_hash
from models import Booking, Schedule, Seat
from extensions import db
from flask_login import current_user
import sys
from sqlalchemy.orm import Session
from sqlalchemy import update
import datetime

book_seat = Blueprint('book_seat_info', __name__)

@book_seat.route('/book_seats/<booking_id>/<seat_number>', methods=['GET', 'POST'])
def book_seats(booking_id, seat_number):
    if current_user.is_authenticated:

        booking = Booking.query.filter_by(
            id=booking_id
        ).first()

        if booking:
            booking.seat_number = seat_number
            #booking.seat_status = 0
            db.session.commit()
        else:
            return "Error booking your seat"
        
        tix = Schedule.query.filter_by(
                id=booking.train_number
            ).first()
        
        seat_all = Seat.query.filter_by(
            train_number=tix.train_number,
            coach_number=booking.coach_number
        ).all()
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
        current_timestamp = datetime.datetime.now()
        
        selected_seat_detail = [
            {
                'id': tix.id,
                'train_number': tix.train_number,
                'origin': tix.origin,
                'destination': tix.destination,
                'departure_time': tix.departure_time.strftime('%H:%M'),
                'arrival_time': tix.arrival_time.strftime('%H:%M'),
                'departure_date': tix.departure_date.isoformat(),
                'price': tix.price,
                'coach_number': booking.coach_number,
                'seat_number': booking.seat_number
            }
        ]
        jsonify({
                'selected_seat_detail': selected_seat_detail
            })
        
        #flash('Booking created successfully with seat number!')
        return render_template('book_seat_info.html', booking_id=booking.id, train_booked=tix.train_number, seat_summary=selected_seat_detail, seat_available=seat_list, current_timestamp=current_timestamp)
    else:
        return "Error: not logged in"