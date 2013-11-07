from setuptools import setup

with open('README.md') as file:
	long_description = file.read()
	
setup(
	author_email = 'astrosilverio@gmail.com',
	name = 'ExpectoCastellum',
	version = '0.5',
	packages=['expectocastellum'],
	license = '',
	long_description = long_description,
	classifiers = [
	'Programming Language :: Python :: 2.7'
	]
)
