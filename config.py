class DevelopmentConfig():
    MONGO_DBNAME = 'moravec'
    MONGO_URI = 'mongodb://localhost:27017/moravec'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://admin:admin@localhost/moravec'


class TestingConfig():
    MONGO_DBNAME = 'moravec'
    MONGO_URI = 'mongodb://localhost:27017/moravec'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/moravec.db'
