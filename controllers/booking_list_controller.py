from flask import Blueprint, request, session, redirect, url_for, flash, jsonify, render_template
from werkzeug.security import check_password_hash
from models import Booking, Schedule, Coach
from extensions import db
from flask_login import current_user
import sys

purchase = Blueprint('purchase_list', __name__)

@purchase.route('/my_tix', methods=['GET', 'POST'])
def my_tix():

    bookings = Booking.query.filter_by(
        customer_email=current_user.email,
        booking_status=1
    ).all()

    print("Bookings:", bookings)

    train_numbers = list(map(int, [booking.train_number for booking in bookings]))
    print("Train Numbers:", train_numbers)


    schedules = Schedule.query.filter(Schedule.id.in_(train_numbers)).all()
    print("Schedules:", schedules)


    schedule_map = {
        schedule.id: {
            'train_number': schedule.train_number,
            'origin': schedule.origin,
            'destination': schedule.destination,
            'departure_date': schedule.departure_date
        }
        for schedule in schedules
    }
    print("Schedule Map:", schedule_map)


    results = []
    for booking in bookings:
        train_number = int(booking.train_number)  
        schedule = schedule_map.get(train_number)
        if schedule:
            results.append({
                'booking_id': booking.id,
                'train_number': schedule['train_number'],
                'origin': schedule['origin'],
                'destination': schedule['destination'],
                'departure_date': schedule['departure_date']
            })
        else:
            results.append({
                'booking_id': booking.id,
                'train_number': None,
                'origin': None,
                'destination': None,
                'departure_date': None
            })

    #return(results)
    return render_template('booking_list.html', results=results)