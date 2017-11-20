#!/usr/bin/env python2
#-*- coding: utf-8 -*-


from flask import current_app
from flask import jsonify
from flask import request
from flask.views import MethodView
from app.base import ApiResource


class Test(ApiResource):
    endpoint = 'Test'
    url_prefix = '/'
    url_rules = {
            'index': {
                'rule': '/',
                },
            'tt': {
                'rule': 'tt',
                }
            }

    def __init__(self):
        MethodView.__init__(self)

    def index(self):
        print 'index'

    def tt(self):
        print 'tt'

    def get(self):
        ret = {}
        rule = request.url_rule.rule 

        for end, endd in self.url_rules.iteritems():
            if self.url_prefix + endd['rule'] == rule:
                getattr(self, end)()
                break
        ret['rule'] = rule

        if request.mimetype == 'application/json':
            ret['code'] = 1
            ret['status'] = 'json'
        else:
            ret['code'] = 1
            ret['status'] = 'not json'

        return jsonify(ret)

    def post(self):
        return self.get()
