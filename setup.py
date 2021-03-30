#!/usr/bin/env python
from setuptools import setup

setup(
    name="singer-tap-informix-odbc",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Axel Bock",
    url="http://flypenguin.de",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["singer_tap_informix_odbc"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
        "pyodbc",
    ],
    entry_points="""
    [console_scripts]
    singer-tap-informix-odbc=singer_tap_informix_odbc:main
    """,
    packages=["singer_tap_informix_odbc"],
    package_data={"schemas": ["singer_tap_informix_odbc/schemas/*.json"]},
    include_package_data=True,
)
