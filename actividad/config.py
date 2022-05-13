from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


class Config:
    pass


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/actividad'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
}
