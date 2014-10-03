#!/usr/bin/python

from distutils.core import setup

setup(name='thorlabs-itc4001',
      version='1.0',
      description="Python interface to Thorlabs ITC4001 laser diode driver",
      author="Ben Gamari",
      author_email="bgamari@physics.umass.edu",
      url="http://goldnerlab.physics.umass.edu/wiki",
      py_modules=['usbtmc'],
      scripts=['thorlabs-laser'],
      data_files=[
              ('/etc/udev/rules.d', ['thorlabs-itc4001.rules']),
      ],
     )
