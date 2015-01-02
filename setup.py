from setuptools import setup, find_packages

setup(
    name='ppxml',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description=('Command-line tool pretty-print XML with xpath'),
    license='MIT',
    keywords='xml',
    url='https://github.com/h2rd/ppxml',
    version='0.2.0',
    packages=find_packages(),
    package_data = {
        '': ['*.md', 'LICENSE'],
    },
    entry_points={
        'console_scripts': ['ppxml = ppxml:main']
    },
    install_requires=[
        'Pygments',
        'lxml',
        'chardet'
    ]
)
