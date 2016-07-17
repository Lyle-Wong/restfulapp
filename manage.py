#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-27 13:59:42
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import BorrowInfo, BookInfo, ReaderInfo

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return dict(app=app, db=db, BookInfo=BookInfo, BorrowInfo=BorrowInfo, ReaderInfo=ReaderInfo)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", 
	Server(host="127.0.0.1", port=5000, use_debugger=True))


if __name__ == '__main__':
	manager.run()