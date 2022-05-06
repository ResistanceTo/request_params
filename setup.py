from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="request_params",
    version="0.0.3",
    description="format request params",
    long_description=long_description,
    author="ResistanceTo",
    author_email="resistanceto@outlook.com",
    url="https://github.com/ResistanceTo/request_params",
    install_requires=[],
    license="GNU GPLv3",
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
