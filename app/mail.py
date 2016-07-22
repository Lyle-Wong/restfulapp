#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 13:12:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import current_app
from flask_mail import Message
from . import mail
from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message("[" + app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + "]" + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = "test"
    msg.html = "<h1>HTML5</h1>"
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
