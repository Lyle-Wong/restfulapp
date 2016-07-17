#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 15:42:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import unittest
from app.models import ReaderInfo


class ReaderInfoTestCase(unittest.TestCase):
	def test_password_setter(self):
		readerinfo = ReaderInfo("000", "王东", "lyle927@yeah.net", 123234213, 1)
		readerinfo.password = "hahahaha"
		self.assertTrue(readerinfo.password_hash is not None)
