import os
from setuptools import setup, find_packages

versions = "0.0.0"
long_description = open('README.txt').read()

setup(
    name = "isotoma.recipe.distros",
    version = versions,
    author = "John Carr",
    author_email = "john.carr@isotoma.com",
    description = "Recipe to install old style products.",
    long_description = long_description,
    license = "ZPL 2.1",
    keywords = "buildout",
    url='http://pypi.python.org/pypi/plone.recipe.distros',
    classifiers=[
      "License :: OSI Approved :: Zope Public License",
      "Framework :: Plone",
      "Framework :: Buildout",
      "Programming Language :: Python",
      ],
    packages = find_packages(),
    include_package_data = True,
    namespace_packages = ['isotoma', 'isotoma.recipe'],
    install_requires = ['zc.buildout', 'setuptools'],
    entry_points = {'zc.buildout': ['default = isotoma.recipe.distros:Recipe']},
    )
