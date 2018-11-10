import os
from abc import ABCMeta


class Config(object, metaclass=ABCMeta):

    DEBUG = False
    TESTING = False

    # Postgresql settings
    DATABASE_URL = os.getenv('DATABASE_URL', None)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class DevelopmentConfig(Config):
    """ Development specific settings """

    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """ testing specific settings """

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """ Production specific settings """


CONFIG_TYPE = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
