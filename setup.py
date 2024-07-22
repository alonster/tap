import os
from setuptools import setup

NAME = 'tap'
DESCRIPTION = 'Generate API docs out of click-based tools.'
URL = 'https://github.com/alonster/tap'
EMAIL = 'alon02st@gmail.com'
AUTHOR = 'Alon S.'
PYTHON_VERSION = '>=3.8.0'
VERSION = '0.1.0'

REQUIRES = [
    'click',
]

root_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root_path, 'README.md')) as f:
    long_description = f.read()

setup(
    name=NAME,
    version='0.1.0',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=PYTHON_VERSION,
    url=URL,
    py_modules=['tap'],
    entry_points={
        'console_scripts': ['tap=tap:tap'],
    },
    install_requires=REQUIRES,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
