from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from models import Schedule  # Import User model
import sys
import json
import html

schedule = Blueprint('train_info', __name__)

@schedule.route('/train_schedule', methods=['POST'])
def train_schedule():
        #print(request.form)
        #sys.exit()
        origin = request.form.get('origins')
        destination = request.form.get('destinations')
        departure = request.form.get('departure')
        return_date = request.form.get('return_date')
        #pax = request.form.get('pax')
        #print(request.form)
        #sys.exit()

        depart_schedules = Schedule.query.filter_by(
            origin=origin,
            destination=destination,
            departure_date=departure
        ).all()
        #print(departure)
        #sys.exit()

        depart_list = [
            {
                'id': schedule.id,
                'train_number': schedule.train_number,
                'origin': schedule.origin,
                'destination': schedule.destination,
                'date': schedule.departure_date.isoformat(),
                'departure_time': schedule.departure_time.strftime('%H:%M'),
                'arrival_time': schedule.arrival_time.strftime('%H:%M'),
                'departure_date': schedule.departure_date.isoformat(),
                'price': schedule.price
            }
            for schedule in depart_schedules
        ]
        
        return_schedules = Schedule.query.filter_by(
            origin=destination,
            destination=origin,
            departure_date=return_date
        ).all()
        
        return_list = [
            {
                'id': schedule.id,
                'train_number': schedule.train_number,
                'origin': schedule.origin,
                'destination': schedule.destination,
                'date': schedule.departure_date.isoformat(),
                'departure_time': schedule.departure_time.strftime('%H:%M'),
                'arrival_time': schedule.arrival_time.strftime('%H:%M'),
                'departure_date': schedule.departure_date.isoformat(),
                'price': schedule.price
            }
            for schedule in return_schedules
        ]

        #json_list = [depart_list, return_list]
        #combined_json = {"depart_list": depart_list, "return_list": return_list}
        
        #return render_template('train_info.html', depart_list=depart_list, return_list=return_list)

        jsonify({
            'depart_schedules': depart_list,
            'return_schedules': return_list
        })

        return render_template('train_info.html', 
            depart_schedules=depart_list,
            return_schedules=return_list
        )
        #return jsonify({
            #'depart_schedules': depart_list,
            #'return_schedules': return_list
        #})


