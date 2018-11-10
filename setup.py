import ast
import re
import sys
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('popresearch/__init__.py', 'rb') as f:
    __version__ = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)
    ))

setup(
    name='popresearch',
    version=__version__,
    description='popresearch project',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'PyYAML==3.11',
        'psycopg2==2.7.5',
        'SQLAlchemy==1.2.8'
    ],
    extras_require={
        'dev': [
            'honcho==1.0.1',
            'alembic==1.0.2'
        ],
        'web': [
            'Flask==1.0.2',
            'Flask-Compress==1.4.0',
            'Flask-RESTful==0.3.6',
            'Flask-SQLAlchemy==2.3.1',
            'gevent==1.3.7',
            'marshmallow==2.16.1',
            'psycogreen==1.0'
        ]
    }
)
