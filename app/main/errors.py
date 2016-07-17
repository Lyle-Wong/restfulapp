#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 14:05:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import render_template
from . import main
from ..mail import send_email


# @main.app_errorhandler(404)
def page_not_found(e):
    #send_email('1060209666@qq.com', 'test', 'test')
    return render_template('404.html'), 404

# @main.app_errorhandler(500)


def server_error(e):
    return render_template('500.html'), 500
