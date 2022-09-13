from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nderp/__init__.py
from nderp import __version__ as version

setup(
	name="nderp",
	version=version,
	description="nderp",
	author="nderp",
	author_email="support@nddb.coop",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
