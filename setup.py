import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_pgk_astfetaw_abera", # Replace with your own username
    version="0.0.1",
    author="Asfetaw Abera",
    author_email="asfetu@gmail.com",
    description="Test Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asfetaw/Helloworld",
    project_urls={
        "Bug Tracker": "https://github.com/Asfetaw/Helloworld",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
