#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 15:55:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import render_template
from . import auth

@auth.route('/login')
def login():
	return render_template('auth/login.html')