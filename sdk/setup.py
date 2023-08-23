# coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="setup.py">
#    Copyright (c) 2018-2023 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

"""
    Aspose.Email Cloud is a REST API for creating email applications that work with common email file formats. It lets developers manipulate message formats such as Outlook MSG, EML and MHT files.
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "aspose-email-cloud"
VERSION = "21.9.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3>=2.0.4",
    "six>=1.16.0",
    "certifi>=2023.7.22",
    "python-dateutil>=2.8.2",
]
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "..", 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    author="Aspose",
    author_email="aspose.email.team@gmail.com",
    description="Aspose.Email Cloud is a REST API for creating email applications that work with common email file formats. It lets developers manipulate message formats such as Outlook MSG, EML and MHT files.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aspose-email-cloud/aspose-email-cloud-python',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    license = "License :: OSI Approved :: MIT License",
    keywords=[
            "Aspose", "Python", "Aspose Cloud",
            "Aspose.Email", "Aspose.Email-Cloud", "Cloud", "REST", "API", "MSG", "EML", "MHTML", "HTML", "VCF", "ICS", "TNEF", "EMLX",
            "iCalendar", "MAPI", "vCard", "Email Conversion", "Convert", "Converter", "Read Email Message", "Calendar", "Email Attachment",
            "Contact Card", "Image to vCard", "Virtual Card", "Search Email", "SMTP", "POP3", "IMAP", "EWS", "WebDav", "SSL Explicit",
            "SSL Implicit", "SSL", "iCalendar", "Email Validation", "OAuth2.0", "Message Thread", "iCalendar Conversion",
            "vCard Conversion", "Email Conversion", "MIME", "Flag Email", "Email Client", "Exchange", "Name API", "name parser",
            "name matcher", "name", "BCR", "contact scan", "business card", "Outlook", "EML to MSG", "MSG to EML", "EML to MHTML",
            "MSG to MHTML", "ICS to MSG", "MSG to ICS", "VCF to MSG", "MSG to VCF", "Disposable email", "email configuration discovery",
            "autodiscover", "email configuration"
        ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRES,
    python_requires='>=3.7',
    project_urls={
        "Documentation": "https://docs.aspose.cloud/email/",
        "Source": "https://github.com/aspose-email-cloud/aspose-email-cloud-python",
        "Website": "https://products.aspose.cloud/email/"
    }
)
