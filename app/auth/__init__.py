#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 15:54:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Blueprint

auth = Blueprint('auth', __name__)


from . import views
