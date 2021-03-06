__author__ = 'slipvyne'

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Message, Mail

app = Flask(__name__)
app.config.from_object('config')

#from .views import mail
mail = Mail(app)
mail.init_app(app)

#from models import db
db = SQLAlchemy(app)

from app.intro_app import views, models
