# setup.py

from setuptools import setup, find_packages

setup(
    name='CacheLayer',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
    ],
    description='Custom caching layer for Django views',
    author='Akash Mothe',
    author_email='motheakash11@gmail.com',
    url='https://github.com/motheakash/CacheLayer.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
