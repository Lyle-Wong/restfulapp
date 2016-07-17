#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 14:04:15
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Blueprint
from flask_restful import Api

main = Blueprint('main', __name__)
api = Api(main)

from . import views, errors
