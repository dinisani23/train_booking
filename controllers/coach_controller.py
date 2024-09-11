from flask import Blueprint, request, session, redirect, url_for, flash, jsonify, render_template
from werkzeug.security import check_password_hash
from models import Booking, Schedule, Coach
from extensions import db
from flask_login import current_user
import sys

coach = Blueprint('coach_info', __name__)

@coach.route('/coaches/<train_number>', methods=['GET', 'POST'])
def coaches(train_number):

    #if 'user_id' not in session:
    if current_user.is_authenticated:
        #flash('You need to log in first.')
        #return redirect(url_for('main.login'))
        user_email = current_user.email
    
        new_booking = Booking(
            train_number=train_number,
            coach_number=None,
            seat_number=None,
            customer_email=user_email 
        )

        db.session.add(new_booking)
        db.session.commit()

        tix = Schedule.query.filter_by(
            id=train_number
        ).first()

        coach_all = Coach.query.filter_by(
            train_number=tix.train_number
        ).all()

        coach_list = [
            {
                'id': coachs.id,
                'train_number': coachs.train_number,
                'coach_number': coachs.coach_number,
                'seat_count': coachs.seat_count
            }
            for coachs in coach_all
        ]

        jsonify({
            'coach_list': coach_list
        })
        #return coach_list

        flash('Booking created successfully with train number!')
        return render_template('coach_info.html', booking_id=new_booking.id, coach_available=coach_list)
        #redirect(url_for('main.coach_info', coach_available=coach_list))
    else:
        #return "Error: not logged in"
        return render_template('sign_up.html')
    
    


