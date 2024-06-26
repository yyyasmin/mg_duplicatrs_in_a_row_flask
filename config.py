import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') or \
        'postgresql://postgres:postgres@localhost:5432/mg_landingpage'

    print("")
    print("IN CONFIG -- SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI)

    #RAILWAY POSTGRES DB
    #postgresql://postgres:SARFxAfgIIsRHwCxVPNVLtZlKuIGCdfH@monorail.proxy.rlwy.net:18915/railway

    WTF_CSRF_ENABLED = True    
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    FLASK_ENV = 'development'