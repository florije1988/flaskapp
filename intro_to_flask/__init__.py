# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask
import os

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.163.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'vob636@163.com'
app.config["MAIL_PASSWORD"] = 'your-password'

from routes import mail

mail.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

from models import db

db.init_app(app)

import intro_to_flask.routes
