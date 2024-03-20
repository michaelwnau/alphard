# This the setup file for the package

from setuptools import setup, find_packages
setup(
    name="alphard",
    version="1.0.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A description of your package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # TODO: Change to Apache License 2.0
        "Operating System :: OS Independent",
    ],
)
