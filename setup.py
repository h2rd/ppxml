from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='ppxml',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description=('Command-line tool pretty-print XML with xpath'),
    long_description=long_description,
    license='MIT',
    keywords='xml',
    url='https://github.com/h2rd/ppxml',
    version='0.1.0',
    packages=find_packages(),
    package_data = { '': ['README.rst', 'LICENSE'] },
    entry_points={ 'console_scripts': ['ppxml = ppxml:main'] },
    install_requires=[ 'Pygments', 'lxml', 'chardet' ]
)
