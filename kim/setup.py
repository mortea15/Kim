#!/usr/bin/env python2
# -*- coding: utf-8-*-
from setuptools import setup

setup(
    name='kim',
    py_modules=['kim'],

    version='0.1',

    description='Personal Assistant for the Raspberry Pi',

    long_description='',

    url='https://github.com/mortea15/kim',

    authors=['Morten Amundsen', 'Svenn-Roger Sørensen', 'Benjamin Gutierrez Børresen', 'Erik Haaland'],

    license='GPL-3.0',

    classifiers=[
        # 3 - Alpha
        # 4 - Beta
        # 5 Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Education',
        'Topic :: Software Development',
        'Topic :: Sound/Audio :: Speech',
        'Topic :: Education',

        'License :: GPL-3.0',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='speech recognition voice control raspberry pi open source education'
)
