__author__ = "hermilocap"
__date__ = "$30/05/2017 10:43:35 AM$"

from setuptools import setup, find_packages

setup (
       name='AlineadorVeeSavi',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='hermilocap',
       author_email='hermilocap@gmail.com',

       summary='Sistema de alineacion automatica de textos paralelos español-mixteco',
       url='',
       license='',
       long_description='Sistema de alineacion automatica de textos paralelos español-mixteco',

       # could also include long_description, download_url, classifiers, etc.
       
       )