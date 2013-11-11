import os

from setuptools import setup, find_packages

setup(
    name='pxml',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description=('Command-line tool to validate and pretty-print XML.'),
    license='MIT',
    keywords='xml',
    url='https://github.com/h2rd/pxml',
    version='0.0.1',
    packages=find_packages(),
    package_data = {
        '': ['*.md', 'LICENSE'],
    },
    entry_points={
        'console_scripts': ['pxml = pxml:main']
    },
    install_requires=[
        'Pygments==1.6'
    ]
)
