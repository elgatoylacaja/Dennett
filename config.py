import os


class Config():
    DEBUG = os.environ['DEBUG']
    DEVELOPMENT = os.environ['DEVELOPMENT']
    TESTING = os.environ['TESTING']
    MONGO_DBNAME = os.environ['MONGO_DBNAME']
    MONGO_URI = os.environ['MONGO_URI']
    SQLALCHEMY_DATABASE_URI = os.environ['SQL_URI']
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
