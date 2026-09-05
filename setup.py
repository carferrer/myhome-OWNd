""" PyPi setup file for OWNd. """

import setuptools

with open("README.md", encoding="utf-8", mode="r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OWNd",
    version="2026.09.05",
    author="carferrer",
    url="https://github.com/carferrer/myhome-OWNd",
    author_email="carferrermar@gmail.com",
    description="Python interface for the OpenWebNet protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["aiohttp", "pytz", "python-dateutil"],
    python_requires=">=3.8",
)
