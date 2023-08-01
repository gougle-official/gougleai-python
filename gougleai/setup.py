from setuptools import setup, find_packages

setup(
    name='gougleai',
    version='1.0.5.1',
    author='Gougle AI LLC',
    author_email='gouglellc@gmail.com',
    description='The Python package for Gougle AI API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://www.github.com/gougle-official/gougleai-python',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)
