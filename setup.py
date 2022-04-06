# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "CRLFsuite",
    version = "1.3.0",
    author = "HS Devansh Raghav",
    license = "MIT",
    keywords = ["CRLFsuite", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/Nefcore/CRLFsuite",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'crlfsuite = crlfsuite.__main__:main'
        ]
    },
)
