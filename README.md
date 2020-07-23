﻿# Aspose.Email Cloud SDK for Python
[![PYPI](https://img.shields.io/pypi/v/aspose-email-cloud)](https://pypi.org/project/aspose-email-cloud/) [![License](https://img.shields.io/github/license/aspose-email-cloud/aspose-email-cloud-python)](https://pypi.org/project/aspose-email-cloud/) ![tests](https://github.com/aspose-email-cloud/aspose-email-cloud-python/workflows/tests/badge.svg)

This repository contains Aspose.Email Cloud SDK for Python source code. This SDK allows you to work with Aspose.Email Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

[Aspose.Email Cloud home](https://products.aspose.cloud/email/family "Aspose.Email Cloud")  
[API Reference](https://apireference.aspose.cloud/email/)

# Key features
Aspose.Email Cloud is a REST API for creating email applications that work with standard email file formats. This SDK:
- Lets developers manipulate different emails’ formats such as Outlook MSG, EML, VCard, and iCalendar files
- Lets developers manipulate different emails' formats such as Outlook MSG, EML, VCard, and iCalendar files
- Supports AI functions:
    - The Business card recognition
    - The Name API for parsing and handling personal names
- Has a built-in email client. This client provides:
    - Unified REST API for different email protocols: IMAP, POP3, SMTP, EWS, WebDav
    - Virtual multi-account
    - Message threads (POP3 accounts are also supported)
- Email configuration discovery
- Disposable email address detection

## New features in version 20.7
- New MAPI message files API with models:
    - `MapiMessageDto` - represents the Microsoft Outlook message.
    - `MapiCalendarDto` - represents the Microsoft Outlook calendar object.
    - `MapiContactDto` - represents the Microsoft Outlook contact information. 
- Improved Recurrence pattern support for CalendarDto.

See [Release notes](https://docs.aspose.cloud/display/emailcloud/Aspose.Email+Cloud+20.7+Release+Notes)

## How to use the SDK?
The complete source code is available in the GIT repository. 

Use [SDK tutorials](https://docs.aspose.cloud/display/emailcloud/SDK+Tutorials):
- [SDK setup](https://docs.aspose.cloud/display/emailcloud/SDK+setup) - installation, account setup, first API calls
- [Business Cards Recognition API](https://docs.aspose.cloud/display/emailcloud/Business+Cards+Recognition+API) - convert captured business cards and name card images, into a vCard format
- [Working with Name API](https://docs.aspose.cloud/display/emailcloud/Working+with+Name+API) - format, genderize, compare, parse, autocomplete names
- [Email Message Files](https://docs.aspose.cloud/display/emailcloud/Email+Message+Files) - Convert EML to MSG and back, edit EML files, etc.
- [Quick Start With iCalendar API](https://docs.aspose.cloud/display/emailcloud/Quick+Start+With+iCalendar+API) - Crate and edit iCalendar files
- [Quick Start With VCard API](https://docs.aspose.cloud/display/emailcloud/Quick+Start+With+VCard+API) - Create and edit VCard files, business card recognition
- [Quick Start With Email Client](https://docs.aspose.cloud/display/emailcloud/Quick+Start+With+Email+Client) - Setup builtin email client, search/fetch/send/move/delete messages
- [Email Client Threads](https://docs.aspose.cloud/display/emailcloud/Email+Client+Threads) - Fetch/Move/Delete email message threads using builtin email client
- [File converters](https://docs.aspose.cloud/display/emailcloud/Convert+Email%2C+Calendar+and+Contact+Files)

SDK reference documentation is available in [this README](sdk/docs/README.md)

### Prerequisites

To use this SDK, you need an App SID and an App Key; they can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/apps) (it requires free registration in Aspose Cloud for this).

### Installation

You can use it directly in your project via the source code or get a [PYPI Package](https://pypi.org/project/aspose-email-cloud/):

    pip install aspose-email-cloud

See more details about SDK installation in this tutorial: [SDK setup](https://docs.aspose.cloud/display/emailcloud/SDK+setup)

### Usage examples

To use the API, you should create an EmailApi object:
```python
from AsposeEmailCloudSdk import api #EmailApi class is here
from AsposeEmailCloudSdk import models #REST API models are here
from AsposeEmailCloudSdk.models import requests #Request models are here (all API calls use corresponding request model class)

#...
app_sid = 'Your App SID'
app_key = 'Your App Key'
email_api = api.EmailApi(app_key, app_sid)
```

#### Business cards recognition API
Use `AiBcrParseModel` method to parse business card image to VCard DTO:
```python
image_data = None
with open('/tmp/alex.png', 'rb') as f:
    filedata = f.read()
    image_data = str(base64.b64encode(filedata), 'utf-8')
result = email_api.ai_bcr_parse_model(requests.AiBcrParseModelRequest(
    models.AiBcrBase64Rq(images=[models.AiBcrBase64Image(True, image_data)])))
contact = result.value[0]
```
See more details [here](https://docs.aspose.cloud/display/emailcloud/Parse+Image+To+VCard+File) and [here](https://docs.aspose.cloud/display/emailcloud/Business+Cards+Recognition+API)

# Licensing
All Aspose.Email Cloud SDKs, helper scripts and templates are licensed under [MIT License](LICENSE).

# Resources
+ [**SDK Reference documentation**](sdk/docs/README.md)
+ [**Website**](https://www.aspose.cloud)
+ [**Product Home**](https://products.aspose.cloud/Email/cloud)
+ [**Documentation**](https://docs.aspose.cloud/display/Emailcloud/Home)
+ [**API Reference**](https://apireference.aspose.cloud/email/)
+ [**Free Support Forum**](https://forum.aspose.cloud/c/email)
+ [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)
+ [**Blog**](https://blog.aspose.cloud/category/aspose-products/aspose-email-cloud/)
+ [**Git repository: Aspose.Email Cloud SDK for .Net**](https://github.com/aspose-email-cloud/aspose-email-cloud-dotnet)
+ [**Git repository: Aspose.Email Cloud SDK for Ruby**](https://github.com/aspose-email-cloud/aspose-email-cloud-ruby)
+ [**Git repository: Aspose.Email Cloud SDK for Python**](https://github.com/aspose-email-cloud/aspose-email-cloud-python)
+ [**Git repository: Aspose.Email Cloud SDK for PHP**](https://github.com/aspose-email-cloud/aspose-email-cloud-php)
+ [**Git repository: Aspose.Email Cloud SDK for Typescript**](https://github.com/aspose-email-cloud/aspose-email-cloud-node)
+ [**Git repository: Aspose.Email Cloud SDK for Java**](https://github.com/aspose-email-cloud/aspose-email-cloud-java)
