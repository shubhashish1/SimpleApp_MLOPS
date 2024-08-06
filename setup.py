from setuptools import setup, find_packages

# Here find_packages will look for the folders containing __init__.py to make them packages.

setup(
    name="src",
    version="0.0.1",
    description="It's a wine Q package",
    author="shubhashish1",
    packages=find_packages(), # To automatically find __init__.py for package creation
    license="MIT" # If we want any other licence then we can create a licence file and put the path here
)