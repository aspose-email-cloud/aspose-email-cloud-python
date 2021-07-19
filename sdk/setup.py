# coding: utf-8

"""
    Aspose.Email Cloud is a REST API for creating email applications that work with common email file formats. It lets developers manipulate message formats such as Outlook MSG, EML and MHT files.
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "aspose-email-cloud"
VERSION = "21.4.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "..", 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    url='https://products.aspose.cloud/email/family',
    classifiers = [
        'License :: OSI Approved :: MIT License',
    ],
    license = "License :: OSI Approved :: MIT License",
    description="Aspose.Email Cloud API",
    author_email="",
    keywords=["Swagger", "Aspose.Email Cloud API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
)
