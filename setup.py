from setuptools import setup, find_packages

setup(
        name='rdmtable',
        version='0.0.0',
        description='Pretty print and query dict of columns',
        author='Riccardo De Maria',
        author_email='riccardo.de.maria@cern.ch',
        url='https://github.com/rdemaria/table',
        packages=find_packages(),
        install_requires=['numpy'],
)
