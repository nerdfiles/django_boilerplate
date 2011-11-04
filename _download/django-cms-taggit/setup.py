#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-cms-taggit',
    version='0.1',
    description='Integration of django-taggit and additional meta data with Django CMS.',
    long_description=open('README.rst').read(),
    author='GW',
    author_email='gw.2011@tnode.com',
    license='GPLv3+',
    url='http://gw.tnode.com/1012-django-cms/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = [
        'django',
        'django-cms',
        'django-taggit',
    ],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
