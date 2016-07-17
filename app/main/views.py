#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 14:01:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

from flask_restful import Resource
from flask import render_template, request, session
from . import main, api

from ..models import BookInfo, BorrowInfo, ReaderInfo
from .. import db
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


class User(Resource):
    """docstring for User"""

    def get(self):
        return {'hello': "world"}

api.add_resource(User, "/")
