class ProductionConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://admin:admin@localhost/moravec'


class DevelopmentConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://admin:admin@localhost/moravec'


class TestingConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/moravec.db'
