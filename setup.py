# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fizzbuzz',
    version='0.1.0',
    description='FizzBuzz exercise in Python',
    long_description=readme,
    author='Dave Nicolette',
    author_email='davenicolette@gmail.com',
    url='https://github.com/neopragma/fizzbuzz-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
