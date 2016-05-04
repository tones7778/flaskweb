import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'test.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'asd8a7d328kdf9s@@0fdsi'

DATABASE_PATH = os.path.join(basedir, DATABASE)