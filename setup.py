#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from setuptools import setup

requirements = [line.strip() for line in open('requirements.txt', 'r').readlines()]
version      = '1.0.8-5'

if os.path.isfile('VERSION'):
    version = open('VERSION', 'r').readline().strip() or version

setup(
    name                = 'dockerator',
    version             = version,
    description         = 'Waycom Dockerator',
    author              = 'Waycom',
    author_email        = 'devs@waycom.net',
    license             = 'Apache License 2.0',
    url                 = 'http://www.waycom.net',
    scripts             = [
        'bin/dockerator'
    ],
    install_requires    = requirements
)
