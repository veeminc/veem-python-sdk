#! /bin/env python

'''Setup file for Veem Python SDK

See:
    https://packaging.python.org/en/latest/distributing.html
'''
import os
import re
from setuptools import find_packages, setup

def read(*file):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           *file)) as f:
        content = f.read()
    return content

def version_info(*args):
    content = read(*args)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              content, re.M)
    if version_match:
        return version_match.group(1)
    return '1.0.0'

# get version information
version = version_info('src', 'veem', '__init__.py')

# launch setup
setup(
    name = 'veem',
    version = version,

    # descriptions
    description = ('Veem Python SDK provides an interface to call '
                   'Veem Global Payments APIs (https://www.veem.com).'),
    long_description = read('DESCRIPTION.md'),
    long_description_content_type='text/markdown',
    author = 'Veem',
    author_email = 'devsupport@veem.com',
    url = 'https://github.com/veeminc/veem-python-sdk',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # project keywords
    keywords = 'veem python sdk b2b payment',

    # uses namespace package
    namespace_packages = [],

    # project packages
    packages = find_packages(where = 'src'),

    # project directory
    package_dir = {
        '': 'src',
    },

    # additional package data files that goes into the package itself
    package_data = {
        '': ['README.md']
    },

    # console entry point
    entry_points = {
    },

    # package dependencies
    install_requires = [
        'six',
        'pyyaml',
        'urllib3',
        'attrdict',
        'requests',
    ],

    # any additional groups of dependencies.
    # install using: $ pip install -e .[dev]
    extras_require = {
    },

    # external modules
    ext_modules = [],

    # unit test suite
    test_suite="",

    # any data files placed outside this package.
    # See: http://docs.python.org/3.4/distutils/setupscript.html
    # format:
    #   [('target', ['list', 'of', 'files'])]
    # where target is sys.prefix/<target>
    data_files = [],

    zip_safe = False,
)
