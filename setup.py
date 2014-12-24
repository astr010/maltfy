#from distutils.core import setup
import os

# Ensuring that Setuptools is install
import ez_setup
ez_setup.use_setuptools()

# Depending on the place in which the project is going to be upgraded
from setuptools import setup
try:
	from pypandoc import convert
	read_md = lambda f: convert(f, 'rst')
except ImportError:
	print("warning: pypandoc module not found, could not convert Markdown to RST")
	read_md = lambda f: open(f, 'r').read()

setup(	name="maltfy",
	version="v0.3.1",
	description="maltfy - maltfy is a library for performing certain automated tasks using i3visio OSINT tools with Maltego.",
	author="Felix Brezo and Yaiza Rubio",
	author_email="contacto@i3visio.com",
	url="http://github.com/i3visio/maltfy",
	license="COPYING",
	packages=["maltfy"],
	long_description=read_md("README.md"),
#	long_description=open('README.md').read(),
	install_requires=[
		"usufy",
		"entify",
		"i3visiotools",
#	"pypandoc",
	],
)

