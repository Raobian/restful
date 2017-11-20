#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from app.base import ApiResource
from flask import Flask

from app.test.views import Test
from app.bian.views import Bian


app = Flask(__name__)
app.register_blueprint(Test.as_blueprint())
app.register_blueprint(Bian.as_blueprint())

