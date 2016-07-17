#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 14:13:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required


class SearchForm(Form):
    search_field = StringField('', validators=[Required()])
