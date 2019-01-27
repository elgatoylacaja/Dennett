import os


class Config():
    DEBUG = os.environ['DEBUG']
    DEVELOPMENT = os.environ['DEVELOPMENT']
    ENVIRONMENT = os.environ['ENVIRONMENT']
    MONGO_DBNAME = os.environ['MONGO_DBNAME']
    MONGO_URI = os.environ['MONGO_URI']
    SECRET_KEY = os.environ['SECRET_KEY']
