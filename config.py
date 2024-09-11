import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///D:/work/dv_flask_mvc/train_booking.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '5fd89bb4cd4dfb86b6bf3828'
