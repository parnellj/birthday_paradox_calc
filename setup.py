try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'Birthday Paradox Calculator',
	'version': '0.1',
	'url': 'https://github.com/parnellj/birthday_paradox_calculator',
	'download_url': 'https://github.com/parnellj/birthday_paradox_calculator',
	'author': 'Justin Parnell',
	'author_email': 'parnell.justin@gmail.com',
	'maintainer': 'Justin Parnell',
	'maintainer_email': 'parnell.justin@gmail.com',
	'classifiers': [],
	'license': 'GNU GPL v3.0',
	'description': 'Demonstrates the birthday paradox by generating sets of birthdays and searching for duplicates.',
	'long_description': 'Demonstrates the birthday paradox by generating sets of birthdays and searching for duplicates.',
	'keywords': '',
	'install_requires': ['nose'],
	'packages': ['birthday_paradox_calculator'],
	'scripts': []
}
	
setup(**config)
