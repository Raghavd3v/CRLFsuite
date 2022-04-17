# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "CRLFsuite",
    version = "1.4.0",
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
