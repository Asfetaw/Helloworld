""" This module contains setup instructions for Hellowrld""""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Helloworld", 
    version="0.0.1",
    author="Asfetaw Abera",
    author_email="asfetu@gmail.com",
    description="Test Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asfetaw/Helloworld",
    license="The Unlicense (Unlicense)",
    project_urls={
        "Bug Tracker": "https://github.com/Asfetaw/Helloworld/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    packages=['Helloworld'],
    python_requires=">=3.6",
)
