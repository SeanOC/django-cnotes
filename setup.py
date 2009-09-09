#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-cnote',
    version='0.3.3',
    description='Django cnotes provides a simple cookie based user notification system.',
    author="Sean O'Connor",
    author_email='sean.b.oconnor@gmail.com',
    url='http://github.com/SeanOC/django-cnotes/tree/master',
    packages=find_packages(),
    keywords='django,middleware,cookies,messaging,notifications',
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
