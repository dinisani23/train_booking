from flask import Blueprint, request, session, redirect, url_for, flash, jsonify, render_template
from werkzeug.security import check_password_hash
from models import Booking, Schedule, Seat
from extensions import db
from flask_login import current_user
import sys
from sqlalchemy.orm import Session
from sqlalchemy import update
import datetime
import stripe
stripe.api_key = "sk_test_51PxlIj1cwRvGuazLYBbSjbBv5qxlxLQq1Jt1zyXZTOWV4AJR9P0XrPfQLf1sPmU1irtktdM9eWya6dait9H32Vl200HEflVj7W"

mock_stripe = Blueprint('mock_booking_payment', __name__)

@mock_stripe.route('/mock_pay/<booking_id>', methods=['GET', 'POST'])
def mock_pay(booking_id):
    #return "sdddsda"
    booking = Booking.query.filter_by(
            id=booking_id
        ).first()
    tix = Schedule.query.filter_by(
                id=booking.train_number
            ).first()
    
    booking_dict = booking.to_dict() if booking else {}
    tix_dict = tix.to_dict() if tix else {}
    
    amount = tix.price
    amount_in_sen = int(amount * 100)
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_in_sen,
            currency="myr",
            payment_method="pm_card_visa",
            confirmation_method='manual',
            confirm=True, 
            return_url='https://localhost:5000/payment_success'
        )

        if booking:
            booking.booking_status = 1
            db.session.commit()
        else:
            return "Payment error."
        
        stripe_response = [{
            'client_secret': payment_intent.client_secret,
            'payment_intent_id': payment_intent.id,
            'status': payment_intent.status,
        }]

        jsonify({
                'stripe_response': stripe_response,
                'booking': booking_dict,
                'tix': tix_dict
            })

        return render_template('payment_success.html', booking_id=booking.id, stripe_response=stripe_response, booking=booking, tix=tix)
    
    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 400
    