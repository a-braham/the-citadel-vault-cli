"""The citadel vault server"""
from setuptools import setup, find_packages

with open("README.rst", "r") as file_obj:
    long_description = file_obj.read()

setup(
    name='citadel',
    version='0.1',
    py_modules=find_packages(),
    install_requires=[
        'Click',
        'pytest',
        'pytest-cov',
        'coverage',
        'coveralls',
    ],
    entry_points='''
        [console_scripts]
        citadel=app.run:main
    ''',
    long_description=long_description,
    author='Abraham Kamau',
    author_email='kirumba.kamau@gmail.com',
    license="MIT",
)
