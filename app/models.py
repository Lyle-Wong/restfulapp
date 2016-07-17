#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 14:01:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from sqlalchemy import Column, Integer, String, Float
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class BookInfo(db.Model):
	__tablename__ = 'bookinfo'
	id = db.Column(db.String(30), primary_key=True)
	name = db.Column(db.String(100))
	code = db.Column(db.String(30), unique=True)
	reserve = db.Column(db.Integer)
	price = db.Column(db.Float)
	total = db.Column(db.Integer)
	remain = db.Column(db.Integer)

	def __init__(self, id, name, code, reserve, price, total, remain):
		self.id = id
		self.name = name
		self.code = code
		self.reserve = reserve
		self.price = price
		self.total = total
		self.remain = remain

	def __repr__(self):
		return '<Book %r>' % self.name

class ReaderInfo(db.Model):
	__tablename__ = 'readerinfo'
	id = db.Column(db.String(30), primary_key=True)
	name = db.Column(db.String(30))
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(30), unique=True)
	phone = db.Column(db.String(20), unique=True)
	keep = db.Column(db.SmallInteger)

	@property
	def password(self):
		raise AttributeError('密码不可读取')
	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


	def __init__(self, id, name, email, phone, keep):
		self.id = id
		self.name = name
		self.email = email
		self.phone = phone
		self.keep = keep

	def __repr__(self):
		return '<ReaderInfo %r>' % self.name


class BorrowInfo(db.Model):
	__tablename__ = 'borrowinfo'
	id = db.Column(db.String(30), primary_key=True)
	readid = db.Column(db.String(30), db.ForeignKey('readerinfo.id'))
	bookid = db.Column(db.String(30), db.ForeignKey('bookinfo.id'))
	starttime = db.Column(db.DateTime)
	planendtime = db.Column(db.DateTime)
	endtime = db.Column(db.DateTime)

	def __init__(self, id, readid, bookid, starttime, planendtime, endtime):
		self.id = id
		self.readid = readid
		self.bookid = bookid
		self.starttime = starttime
		self.planendtime = planendtime
		self.endtime = endtime