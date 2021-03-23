# Manage Emails in Cloud via Python REST SDK
[![PYPI](https://img.shields.io/pypi/v/aspose-email-cloud)](https://pypi.org/project/aspose-email-cloud/) [![License](https://img.shields.io/github/license/aspose-email-cloud/aspose-email-cloud-python)](https://pypi.org/project/aspose-email-cloud/) ![tests](https://github.com/aspose-email-cloud/aspose-email-cloud-python/workflows/tests/badge.svg)

[Aspose.Email Cloud SDK for Python](https://products.aspose.cloud/email/python) is a REST API SDK for creating email applications that work with standard email file formats such as Outlook MSG, EML, iCalendar files and VCard.

This SDK allows you to work with Aspose.Email Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

[Aspose.Email Cloud home](https://products.aspose.cloud/email/family)

[Swagger UI](https://apireference.aspose.cloud/email/)

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

## Enhancements in Version 21.3

- IMAP native threads support added to the built-in Email client.
- New field ClientThreadMoveRequest.SourceFolder added to specify a folder to move a thread from.

See [Release notes](https://docs.aspose.cloud/email/aspose-email-cloud-21-3-release-notes/).

## How to use the SDK?
The complete source code is available in the [GIT repository](https://github.com/aspose-email-cloud/aspose-email-cloud-python/tree/master/sdk/AsposeEmailCloudSdk).

Use [SDK tutorials](https://docs.aspose.cloud/email/sdk-tutorials/) and [SDK reference documentation](https://docs.aspose.cloud/email/reference-api/).

### Prerequisites

To use this SDK, you need a Client id and a Client secret; they can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/apps) (it requires free registration in Aspose Cloud for this).

### Installation

You can use it directly in your project via the source code or get a [PYPI Package](https://pypi.org/project/aspose-email-cloud/):

    pip install aspose-email-cloud

See more details about SDK installation in this tutorial: [SDK setup](https://docs.aspose.cloud/email/sdk-setup/).

### Usage examples

To use the API, you should create an EmailCloud object:
```python
from AsposeEmailCloudSdk import api #EmailApi class is here
from AsposeEmailCloudSdk import models #REST API models are here

#...
client_secret = 'Your Client secret'
client_id = 'Your Client id'

email_cloud = api.EmailCloud(client_secret, client_id)
```

#### Business cards recognition API
Use `AiBcrApi.parse` method to parse business card image to VCard DTO:
```python
path = 'path/to/image/to/parse.png'
result = email_cloud.ai.bcr.parse(models.AiBcrParseRequest(image_file))
contact = result.value[0]
assert 'Parsed Display Name' in contact.display_name
```

[Product Page](https://products.aspose.cloud/email/python) | [Documentation](https://docs.aspose.cloud/email/) | [Demo](https://products.aspose.app/email/family) | [Swagger UI](https://apireference.aspose.cloud/email/) | [Blog](https://blog.aspose.cloud/category/email/) | [Free support](https://forum.aspose.cloud/c/email) | [Free trial](https://dashboard.aspose.cloud/#/apps) | [SDK reference documentation](https://docs.aspose.cloud/email/reference-api)