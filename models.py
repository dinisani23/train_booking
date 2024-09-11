from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extensions import db

#db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    bookings = db.relationship('Booking', backref='user', lazy=True)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)


class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    train_number = db.Column(db.String(20), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)

    coaches = db.relationship('Coach', backref='schedule', lazy=True)
    bookings = db.relationship('Booking', backref='schedule', lazy=True, 
                               primaryjoin="Schedule.train_number == Booking.train_number")
    
    def to_dict(self):
        return {
            'id': self.id,
            'train_number': self.train_number,
            'origin': self.origin,
            'destination': self.destination,
            'departure_time': self.departure_time.strftime('%H:%M'),
            'arrival_time': self.arrival_time.strftime('%H:%M'),
            'departure_date': self.departure_date.isoformat(),
            'price': self.price
        }


class Coach(db.Model):
    __tablename__ = 'coaches'
    id = db.Column(db.Integer, primary_key=True)
    train_number = db.Column(db.String(20), db.ForeignKey('schedules.train_number'), nullable=False)
    coach_number = db.Column(db.Integer, nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)

    seats = db.relationship('Seat', backref='coach', lazy=True)
    
    __table_args__ = (
        db.UniqueConstraint('train_number', 'coach_number'),
    )


class Seat(db.Model):
    __tablename__ = 'seats'
    id = db.Column(db.Integer, primary_key=True)
    train_number = db.Column(db.String(20), nullable=False)
    coach_number = db.Column(db.Integer, nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    seat_status = db.Column(db.Integer, default=1, nullable=False)
    locked_until = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['train_number', 'coach_number'],
            ['coaches.train_number', 'coaches.coach_number']
        ),
        db.UniqueConstraint('train_number', 'coach_number', 'seat_number'),
    )


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    train_number = db.Column(db.String(20), db.ForeignKey('schedules.train_number'), nullable=False)
    coach_number = db.Column(db.Integer, nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    customer_email = db.Column(db.String(120), db.ForeignKey('users.email'), nullable=False)
    #booking_date = db.Column(db.Date, nullable=False)
    #booking_date = Column(DateTime, server_default=func.now())
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    booking_status = db.Column(db.Integer, default=0, nullable=False)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['train_number', 'coach_number', 'seat_number'],
            ['seats.train_number', 'seats.coach_number', 'seats.seat_number']
        ),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'train_number': self.train_number,
            'coach_number': self.coach_number,
            'seat_number': self.seat_number,
            'customer_email': self.customer_email,
            'booking_date': self.booking_date.isoformat(),
            'booking_status': self.booking_status
        }
