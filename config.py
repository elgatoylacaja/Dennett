class ProductionConfig():
    DEBUG = False
    DATABASE_URI = ''

class DevelopmentConfig():
    DEBUG = True
    DATABASE_URI = 'postgres://admin:admin@localhost/moravec'

class TestingConfig():
    DEBUG = False
    DATABASE_URI = 'postgres://admin:admin@localhost/moravec'
