from sqlalchemy import create_engine, exc


class Config:
    pass


class DevelopmentConfig(Config):

    DEBUG = True
    import time
    while 1:
        try:
            e = create_engine('postgresql://postgres:postgres@postgres:5432/actividad')
            e.connect()
            e.execute('select 1')
        except exc.OperationalError:
            print('Waiting for database...')
            time.sleep(1)
        else:
            break
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/actividad'

config = {
    'development': DevelopmentConfig,
}
