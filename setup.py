#!/usr/bin/env python

from setuptools import setup

setup(
    name='haikuthegibson',
    version='1.0.0',
    description='tweetbot of haiku from Hackers script',
    url='https://github.com/nathanielksmith/haikuthegibson',
    author='vilmibm shaksfrpease',
    author_email='nks@lambdaphil.es',
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
    keywords='poetry',
    packages=['haikuthegibson'],
    install_requires = ['prosaic==5.1.0', 'tweepy==3.5.0',],
    entry_points = {
          'console_scripts': [
              'haikuthegibson  = haikuthegibson.__init__:main'
          ]
    },
)
