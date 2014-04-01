# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
import os
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version(package):
    """Return package version as listed in `__version__` in `__init__.py`."""
    init_py = open(os.path.join(os.path.dirname(__file__),
                                package, '__init__.py'),
                   'r').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE
    ).group(1)

extra = {}

if sys.version_info >= (3,):
    extra['use_2to3'] = True
    #extra['convert_2to3_doctests'] = ['src/your/module/README.txt']
    #extra['use_2to3_fixers'] = ['your.fixers']
    #extra['install_requires'] = ['distribute',]
    #extra['tests_require'] = ['pep8>=0.6.1','pep8<1.3',],
#else:
#    extra['install_requires'] = ['reportlab>=2.5',]
#    extra['tests_require'] = ['pep8>=0.6.1','pep8<1.3','pyflakes>=0.5.0',]

setup(
    name='pycrackcaptcha',
    version=get_version('pycrackcaptcha'),
    author= u'Alexandre Defendi - Evoluir Informática',
    author_email='alexandre@evoluirinformatica.com.br',
    url='',
    packages=find_packages(),
    package_data={
        '': ['LICENSE'],
    },
    zip_safe=False,
    provides=[
    ],
    license='BSD',
    description='Python Library to crack captchas',
    long_description=read('README.rst'),
    download_url='',
    scripts=[],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    **extra
)
