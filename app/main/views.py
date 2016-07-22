#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 14:01:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

import uuid
from flask_restful import Resource, reqparse, abort
from flask import render_template, request, session, jsonify, g
from . import main, api

from ..models import BookInfo, BorrowInfo, ReaderInfo
from .. import db, auth
from ..mail import send_email


# @main.route('/', methods=['GET', 'POST'])
# def index(default=''):
#     return render_template('index.html')


# @main.route('/books', methods=['GET', 'POST'])
# def book():
#     books = BookInfo.query.all()
#     return render_template('books.html',
#                            books=books)


# @main.route('/borrow', methods=['GET', 'POST'])
# def borrow():
#     borrows = db.session.query(BorrowInfo, ReaderInfo, BookInfo).join(
#         ReaderInfo).join(BookInfo).all()
#     return render_template('borrows.html',
#                            borrows=borrows)

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = ReaderInfo.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = ReaderInfo.query.filter_by(name=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@main.route('/index')
def index():
	return render_template('index.html')


class User(Resource):
    """docstring for User"""

    @auth.login_required
    def get(self):
        return jsonify({'hello': ""})

    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        if username is None or password is None:
            abort(403, message="username or password null")
        if ReaderInfo.query.filter_by(name=username).first() is not None:
            abort(409)
        idd = uuid.uuid4().hex
        reader = ReaderInfo(id=idd, name=username,
                            email="web@web.com", phone="12313123")
        reader.password = password
        db.session.add(reader)
        db.session.commit()
        return jsonify(name=username, password=password)

api.add_resource(User, "/")
