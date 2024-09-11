from flask import Flask
from config import Config
from extensions import db, migrate, login_manager  # Import db and migrate from extensions.py

app = Flask(__name__)  # Initialize the Flask app
app.config.from_object(Config)

db.init_app(app)  # Initialize the db with the app
migrate.init_app(app, db)  # Initialize Flask-Migrate
login_manager.init_app(app)


from models import User  # Adjust import based on your structure

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from controllers.main_controller import main as main_blueprint
from controllers.login_controller import login as login_blueprint
from controllers.train_controller import schedule as train_blueprint
from controllers.coach_controller import coach as coach_blueprint
from controllers.seat_controller import seat as seat_blueprint
from controllers.book_seat_controller import book_seat as book_seat_blueprint
from controllers.confirm_tix_controller import confirm_tix as confirm_tix_blueprint
from controllers.mock_payment_controller import mock_stripe as mock_payment_blueprint
from controllers.booking_list_controller import purchase as booking_list_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(train_blueprint)
app.register_blueprint(coach_blueprint)
app.register_blueprint(seat_blueprint)
app.register_blueprint(book_seat_blueprint)
app.register_blueprint(confirm_tix_blueprint)
app.register_blueprint(mock_payment_blueprint)
app.register_blueprint(booking_list_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
