#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 14:00:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_httpauth import HTTPBasicAuth
from config import config

mail = Mail()
db = SQLAlchemy()
auth = HTTPBasicAuth()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    # auth.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
