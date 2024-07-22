import os

class Config:
    SECRET_KEY = os.environ.get('main')
    DEBUG = True
