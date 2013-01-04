# -*- coding: utf8 -*-

from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='collective.contact.content',
      version=version,
      description="Dexterity contact content type",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='"Cédric Messiant"',
      author_email='cedricmessiant@ecreall.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.contact'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.contact.vcard',
          'collective.z3cform.datagridfield',
          'setuptools',
          'five.grok',
          'five.globalrequest',
          'plone.app.dexterity',
          'plone.app.relationfield',
          'plone.supermodel',
          'plone.autoform',
          'Products.CMFPlone',
      ],
      extras_require={
          'test': ['plone.app.testing',
                   'ecreall.helpers.testing',
                   ],
          },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
