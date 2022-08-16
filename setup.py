# -*- coding: utf-8 -*-
import warnings
from setuptools import setup, find_packages
warnings.filterwarnings('ignore')

setup(
    name = "CRLFsuite",
    version = "2.5.2",
    author = "HS Devansh Raghav",
    license = "MIT",
    keywords = ["CRLFsuite", "Bug Bounty", "pentesting", "security", "CRLF Injection"],
    url = "https://github.com/Nefcore/CRLFsuite",
    packages=find_packages(),
    package_data={'crlfsuite': ['db/*']},
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