from setuptools import setup, find_packages

setup(
    name='gougleai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Gougle',
    description='Gougle AI library for Python',
    url='https://github.com/gougle-official/gougleai-python',
    keywords='gougle ai machine-learning deep-learning',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GPL V3.0',
        'Operating System :: OS Independent',
    ],
)
