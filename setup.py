from setuptools import setup

with open('README.txt') as file:
	long_description = file.read()
	
setup(
	name = 'ExpectoCastellum',
	version = '0.1dev1',
	packages=['expectocastellum'],
	license = '',
	long_description = long_description,
	install_requires = ['subprocess']
	classifiers=['Programming Language :: Python :: 2.7']
)
