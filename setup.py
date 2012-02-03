#! /usr/bin/env python
from setuptools import setup, find_packages

# dynamic retrive version number from stachless.VERSION
version_tuple = __import__('django_images').VERSION
version = '.'.join([str(v) for v in version_tuple])

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

REQUIREMENTS = [
    'Django >= 1.3',
]

setup(name='django-images',
      author='Mirumee Software',
      author_email='hello@mirumee.com',
      description='A database-driver thumbnailing solution for Django',
      license='BSD',
      version=version,
      packages=find_packages(),
      include_package_data=True,
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      platforms=['any'])
