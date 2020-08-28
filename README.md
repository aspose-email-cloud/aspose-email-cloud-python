# Manage Emails in Cloud via Python REST SDK
[![PYPI](https://img.shields.io/pypi/v/aspose-email-cloud)](https://pypi.org/project/aspose-email-cloud/) [![License](https://img.shields.io/github/license/aspose-email-cloud/aspose-email-cloud-python)](https://pypi.org/project/aspose-email-cloud/) ![tests](https://github.com/aspose-email-cloud/aspose-email-cloud-python/workflows/tests/badge.svg)

[Aspose.Email Cloud SDK for Python](https://products.aspose.cloud/email/python) is a REST API SDK for creating email applications that work with standard email file formats such as Outlook MSG, EML, iCalendar files and VCard.

This SDK allows you to work with Aspose.Email Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

[Aspose.Email Cloud home](https://products.aspose.cloud/email/family)
[API Reference](https://apireference.aspose.cloud/email/)

# Cloud Email Processing Features
Aspose.Email Cloud is a REST API for creating email applications that work with standard email file formats. This SDK:
- Lets developers manipulate different emails' formats such as Outlook MSG, EML, VCard, and iCalendar files.
- Supports AI functions:
    - The Business card recognition.
    - The Name API for parsing and handling personal names.
- Has a built-in email client. This client provides:
    - Unified REST API for different email protocols: IMAP, POP3, SMTP, EWS, WebDav.
    - Virtual multi-account.
    - Message threads (POP3 accounts are also supported).
- Email configuration discovery.
- Disposable email address detection.

## New features in version 20.9

Aspose.Email Cloud SDK 20.9.0 is based on a new v4.0 REST API.

- All SDK functions are divided into groups (Email, Calendar, Contact, Client, Ai, Mapi, etc.).
- Unified file API provided for supported file types (Save, Get, Convert, AsFile, FromFile, AsMapi/AsDto).
- HierarchicalObject based API is removed.
- All models are stored in one folder/namespace.
- The request models are simplified.

See [Release notes](https://docs.aspose.cloud/display/emailcloud/Aspose.Email+Cloud+20.9+Release+Notes).

## How to use the SDK?
The complete source code is available in the [GIT repository](https://github.com/aspose-email-cloud/aspose-email-cloud-python/tree/master/sdk/AsposeEmailCloudSdk).

Use [SDK tutorials](https://docs.aspose.cloud/display/emailcloud/SDK+Tutorials).

SDK reference documentation is available in [this README](https://github.com/aspose-email-cloud/aspose-email-cloud-python/blob/master/sdk/docs/README.md).

### Prerequisites

To use this SDK, you need an App SID and an App Key; they can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/apps) (it requires free registration in Aspose Cloud for this).

### Installation

You can use it directly in your project via the source code or get a [PYPI Package](https://pypi.org/project/aspose-email-cloud/):

    pip install aspose-email-cloud

See more details about SDK installation in this tutorial: [SDK setup](https://docs.aspose.cloud/display/emailcloud/SDK+setup).

### Usage examples

To use the API, you should create an EmailCloud object:
```python
from AsposeEmailCloudSdk import api #EmailApi class is here
from AsposeEmailCloudSdk import models #REST API models are here

#...
app_sid = 'Your App SID'
app_key = 'Your App Key'
email_cloud = api.EmailCloud(app_key, app_sid)
```

#### Business cards recognition API
Use `AiBcrApi.parse` method to parse business card image to VCard DTO:
```python
path = 'path/to/image/to/parse.png'
result = email_cloud.ai.bcr.parse(models.AiBcrParseRequest(image_file))
contact = result.value[0]
assert 'Parsed Display Name' in contact.display_name
```

[Product Page](https://products.aspose.cloud/email/python) | [Documentation](https://docs.aspose.cloud/display/Emailcloud/Home) | [Demo](https://products.aspose.app/email/family) | [API Reference](https://apireference.aspose.cloud/email/) | [Blog](https://blog.aspose.cloud/category/email/) | [Free support](https://forum.aspose.cloud/c/email) | [Free trial](https://dashboard.aspose.cloud/#/apps)