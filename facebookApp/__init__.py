from flask import Flask

from .views import app
from . import models

# app=Flask(__name__)

# @app.route('/')
# def index():
# return "Hello World !"

# if __name__=="__main__":
# app.run()

models.db.init_app(app)

@app.cli.command()
def init_db():
    models.init_db()