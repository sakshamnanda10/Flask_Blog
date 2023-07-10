import os


class Config:
    WTF_CSRF_CHECK_DEFAULT = False
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =  os.environ.get('SQLALCHEMY_DATABASE_URI')