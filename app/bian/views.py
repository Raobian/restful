#!/usr/bin/env python2
#-*- coding: utf-8 -*-


from flask import current_app
from flask import jsonify
from flask import request
from flask.views import MethodView
from app.base import ApiResource


class Bian(ApiResource):
    endpoint = 'Bian'
    url_prefix = '/bian'
    url_rules = {
            'index': {
                'rule': '/',
                },
            'pp': {
                'rule': '/pp',
                },
            }

    def __init__(self):
        MethodView.__init__(self)

    def get(self):
        return jsonify({'code': 1, 'status': 'success'})

    def post(self):
        return self.get()
