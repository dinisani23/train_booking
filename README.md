# Train Ticket Booking System

## Overview
This web application is a Train Ticket Booking System built using Flask. It allows users to browse train schedules, book seats, and manage their bookings. The system integrates with a mock payment gateway for payment processing and includes user authentication features.

## Features
### User Authentication:
- User Sign-Up
- User Login
- User Logout
  
### Train Information:
- View train schedules

### Coach Information:
- View available coaches for a specific train

### Seat Reservation:
- Select and book seats on a coach

### Booking Management:
- View and manage your bookings

Payment Processing:
- Complete payments via Stripe (mock setup for testing)

## Requirements
- Python 3.x
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- Stripe (for payment processing)

## Configuration
Stripe Configuration: Replace the Stripe test key in the mock_stripe Blueprint with actual Stripe test key.

## Testing
To test the payment functionality, use the mock payment route:

GET /mock_pay/<booking_id>: Initiates a mock payment for the specified booking ID.
