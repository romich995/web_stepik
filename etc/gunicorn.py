#! /usr/bin/env python
# -*- coding: utf-8 -*-
bind = "0.0.0.0:8080"
pythonpath= "/home/box/web"
# или через сокет
# bind = "unix:/home/proft/projects/blog/run/blog.socket"
workers = 5
user = "www-data"
group = "www-data"
logfile = "/home/box/web/etc/gunicorn.log"
loglevel = "info"
proc_name = "blog"
