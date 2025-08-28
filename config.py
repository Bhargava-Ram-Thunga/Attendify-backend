# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A_REALLY_SECRET_AND_HARD_TO_GUESS_KEY'
    MONGO_URI = 'mongodb+srv://br5183268_db_user:5OYRptTxnfDDzoB3@all-data.1yx5m91.mongodb.net/'
    DATABASE_NAME = 'Attendify'