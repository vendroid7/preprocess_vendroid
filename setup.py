import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_vendroid', #this should be unique
	version = '1.0.4',
	author = 'Venkatesh Iyer',
	author_email = 'venkateshiyer00@gmail.com',
	description = 'This is preprocessing package for textual data',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.7'
	)