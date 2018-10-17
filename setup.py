#!/usr/bin/env python

import setuptools
from distutils.core import setup
import os

# Get the long description from the README file
with open(os.path.join(".", "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ascvd",
    version="0.5",
    description="Module for calculating ASCVD 10-year estimate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brandon Istenes",
    author_email="brandonesbox@gmail.com",
    url="https://github.com/brandones/ascvd",
    packages=["ascvd"],
    project_urls={"Source": "https://github.com/brandones/ascvd"},
)
