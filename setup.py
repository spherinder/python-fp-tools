import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-fp-tools-spherinder", # Replace with your own username
    version="0.0.1",
    author="spherinder",
    author_email="spherinder@gmail.com",
    description="A package for functional programming in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spherinder/python-fp-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
