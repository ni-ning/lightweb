# -*- coding:utf-8 -*-

from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

sdict = {
    'name': 'lightmail',
    'version': '1.0.0',
    'keywords': 'Django, Request, Response',
    'packages': [
        'lightweb'
    ],
    'install_requires': requirements,
    'zip_safe': False,
    'description': 'Light Web Utility for Django',
    'long_description': long_description,
    'url': 'https://github.com/ni-ning/lightweb',
    'author': 'ni-ning',
    'author_email': 'nining1314@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    'include_package_data': True
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if __name__ == '__main__':
    setup(**sdict)
