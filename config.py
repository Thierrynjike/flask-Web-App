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

# This will indicate where our database is located to check it
