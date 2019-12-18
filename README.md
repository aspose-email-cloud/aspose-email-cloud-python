# Aspose.Email Cloud SDK for Python [![PYPI](https://img.shields.io/pypi/v/aspose-email-cloud)](https://pypi.org/project/aspose-email-cloud/) [![License](https://img.shields.io/github/license/aspose-email-cloud/aspose-email-cloud-python)](https://pypi.org/project/aspose-email-cloud/)
This repository contains Aspose.Email Cloud SDK for Python source code. This SDK allows you to work with Aspose.Email Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

[Aspose.Email Cloud home](https://products.aspose.cloud/email/family "Aspose.Email Cloud")  
[API Reference](https://apireference.aspose.cloud/email/)

# Key features

Aspose.Email Cloud is a REST API for creating email applications that work with standard email file formats. This SDK:
- Lets developers manipulate different emails’ formats such as Outlook MSG, EML, VCard, and iCalendar files
- Has a built-in email client
- Supports AI functionalities:
    - The Business card recognition
    - The Name API for parsing and handling personal names

## How to use the SDK?
The complete source code is available in the GIT repository. 
Use reference documentation, available [**here**](sdk/docs/README.md)

### Prerequisites

To use this SDK, you need an App SID and an App Key; they can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/apps) (it requires free registration in Aspose Cloud for this).

### Installation

You can use it directly in your project via the source code or get a [PYPI Package](https://pypi.org/project/aspose-email-cloud/):

    pip install aspose-email-cloud


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

API calls can be synchronous or asynchronous (using ThreadPool from multiprocessing.pool):
```python
result = email_api.get_calendar(
    requests.GetCalendarRequest(
        calendar_file,
        folder,
        storage))
# or
async_result = email_api.get_calendar_async( #returns multiprocessing.pool.AsyncResult
    requests.GetCalendarRequest(
        calendar_file,
        folder,
        storage))
result = async_result.get()
```

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