#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'dojo.views.newdojo'),
    (r'^create$', 'dojo.views.create'),
)
