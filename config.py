#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 13:59:27
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'afhaouhfashgpas;fn;asdhfa;ghuars'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/bookms'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{url}//bookms.db'.format(
        url=basedir[3:]).replace("\\", "//")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    TABLE_PREFIX = 't_'

    MAIL_SERVER = 'smtp.yeah.net'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'lyle927@yeah.net'
    MAIL_PASSWORD = '**'

    FLASKY_MAIL_SUBJECT_PREFIX = 'Lyle'
    FLASKY_MAIL_SENDER = 'Wang Lei<lyle927@yeah.net>'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
