# configuration file for tests

import os  # this line were added when we started to use the db

FB_APP_ID = 698522940978347

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])

# The following instructions were added when we started to use the db
# os.path.abspath will find the path

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10
SERVER_NAME = 'localhost:8943'

#facebook test user informations

FB_USER_NAME = "lapache titi"
FB_USER_PW = "azerty1234"
FB_USER_EMAIL = "lapache_krvjpgv_titi@tfbnw.net	M"
FB_USER_ID = 101218878202104
FB_USER_GENDER = 'male'
# This will indicate where our database is located to check it
