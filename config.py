import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c219cad489c95a9ddfdda573af021c0f'