from setuptools import setup, find_packages

setup(
    name='couchdb_api',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'httpx'
    ]
)
