from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in logicaldna/__init__.py
from logicaldna import __version__ as version

setup(
	name="logicaldna",
	version=version,
	description="plant-maintanence",
	author="shreyas",
	author_email="shreyasnaik01@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
