#! /usr/bin/env python
# -*- coding: utf-8 -*-

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes(s+'\n','ascii') for s in env['QUERY_STRING'].split("&")]
