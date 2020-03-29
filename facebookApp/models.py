from flask import Flask
import logging as lg
from flask_sqlalchemy import SQLAlchemy as sqla

from .views import app

# Create database connection object
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = sqla(app)


# we create a new type of object(a table)


class Content(db.Model):
    # creation of columns in the table content
    id = db.Column(db.Integer, primary_key=True)  # primaryKey
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Integer(), nullable=False)

    # definition of the constructor to create a new object

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


db.create_all()


# create the database

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content('This is Spartaaaaa!!!', 1))
    db.session.add(Content('What is your favorite scary movie?', 0))
    db.session.add(Content('What is your name?', 2))
    db.session.commit()
    lg.warning('Database initialized!')
