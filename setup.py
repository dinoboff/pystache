#!/usr/bin/env python

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

import os
import sys

from setuptools import setup

def publish():
    """Publish to Pypi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(name='pystache',
      version='0.3.0',
      description='Mustache for Python',
      long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
      author='Chris Wanstrath',
      author_email='chris@ozmm.org',
      url='http://github.com/defunkt/pystache',
      packages=['pystache', 'pystache.examples', 'pystache.tests'],
      test_suite='pystache.tests',
      use_2to3=True,
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      classifiers=(
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        )
     )

