#! /usr/bin/env python
# -*- coding: utf-8 -*-

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [str(s+'\n') for s in env['QUERY_STRING'].split("&")]
