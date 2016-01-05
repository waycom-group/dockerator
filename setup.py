#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

requirements = [
    "pyyaml==3.10",
    "docker-py",
]

setup(
    name                = 'dockerator',
    version             = '1.0.5-3',
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
