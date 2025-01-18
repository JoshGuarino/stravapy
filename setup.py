from setuptools import setup, find_packages

setup(
    name='stravapy',
    version='0.1.0',
    description='Stravapy is a python 3 sdk for interacting with the Strava API v3.',
    author='Josh Guarino',
    author_email='jguarino722@gmail.com',
    packages=find_packages('stravapy', exclude=['tests'])
)
