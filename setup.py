from setuptools import setup, find_packages

setup(
    name='pxml',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description=('Command-line tool pretty-print XML with xpath'),
    license='MIT',
    keywords='xml',
    url='https://github.com/h2rd/pxml',
    version='0.2.0',
    packages=find_packages(),
    package_data = {
        '': ['*.md', 'LICENSE'],
    },
    entry_points={
        'console_scripts': ['pxml = pxml:main']
    },
    install_requires=[
        'Pygments==1.6',
        'lxml==3.2.5'
    ]
)
