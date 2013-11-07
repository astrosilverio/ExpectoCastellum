from setuptools import setup

with open('README.txt') as file:
	long_description = file.read()
	
setup(
	author_email = 'astrosilverio@gmail.com'
	name = 'ExpectoCastellum',
	version = '0.1',
	packages=['expectocastellum'],
	license = '',
	long_description = long_description,
	install_requires = ['subprocess', 'json', 'os', 'random'],
	classifiers = [
	'Programming Language :: Python :: 2.7'
	]
)
