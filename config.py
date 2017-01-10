class ProductionConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    DATABASE_URI = ''

class DevelopmentConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DATABASE_URI = 'postgres://admin:admin@localhost/moravec'

class TestingConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DATABASE_URI = 'postgres://admin:admin@localhost/moravec'
