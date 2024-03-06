import os
from setuptools import setup, find_packages

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

setup(
    name='gougleai',
    version='1.0.5.2',
    author='Gougle AI LLC',
    author_email='gouglellc@gmail.com',
    description='The Python package for Gougle AI API.',
    long_description=open(os.path.join(parent_dir, 'README.md'), "r").read(),
    long_description_content_type='text/markdown',
    url='https://www.github.com/gougle-official/gougleai-python',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
    package_data={'': ['../LICENSE']}
)
