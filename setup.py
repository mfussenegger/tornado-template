#!/usr/bin/env python
# -*- coding: utf-8 -*-


from SITENAME import __version__

import os
from distutils.core import setup

readmes = ['README', 'README.rst', 'README.md']

readme = ''
for readmef in readmes:
    if os.path.isfile(readmef):
        readme = open(readmef).read()


setup(
    name='SITENAME',
    version=__version__,
    author='Your Name',
    author_email='your@email.com',
    url='http://project.url',
    license='MIT',
    description='template for tornado projects',
    long_description=readme,
    packages=['SITENAME'],
    platforms=['any']
)
