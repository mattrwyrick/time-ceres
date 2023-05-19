import os

from distutils.core import setup
from setuptools import find_packages

current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''


setup(
    name="Time-Ceres",
    packages=find_packages('.'),
    version='1.0.0',
    license='',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='',
    long_description = long_description,
    long_description_context_type = 'text/markdown',
    author='Matt Wyrick',
    author_email='mattrwyrick@gmail.com',
    url='https://github.com/mattrwyrick/time-ceres',
    download_url='',
    keywords=["forecast", "explainable", "analytics"],
    install_requires=[],
    classifiers=[]  # https://pypi.org/classifiers/
)