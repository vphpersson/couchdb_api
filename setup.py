from setuptools import setup, find_packages

setup(
    name='couchdb_api',
    version='0.27',
    packages=find_packages(),
    install_requires=[
        'httpx==0.23.3'
    ]
)
