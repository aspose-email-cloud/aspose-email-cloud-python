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

#### Business cards recognition API
See examples below:

<details open>
    <summary>Parse business card images to VCard contact files</summary>

```python
storage = 'First Storage' # Your storage name
file_name = 'some_file_name.png' #Supports different image formats: PNG, JPEG, BMP, TIFF, GIF, etc.
image_file = 'some/business/card/image/file/on/disk.png'
folder = 'some/folder/path/on/storage'
# Upload business card image to storage
storage_location = folder + '/' + file_name
email_api.upload_file(
    requests.UploadFileRequest(storage_location, image_file, storage))

out_folder_path = 'some/other/folder/path/on/storage' # Business card recognition results will be saved here
email_api.create_folder(requests.CreateFolderRequest(out_folder_path, storage))
# Call business card recognition action
result = email_api.ai_bcr_parse_storage(requests.AiBcrParseStorageRequest(
    models.AiBcrParseStorageRq(
        images=[
            models.AiBcrImageStorageFile(
                True, #Flag isSingle determines that image contains single VCard or more.
                      #Only single VCard on image variant is supported in current version.
                models.StorageFileLocation(storage, folder, file_name))],
        out_folder=models.StorageFolderLocation(storage, out_folder_path))))
# Get file name from recognition result
contact_file = result.value[0] # result.value can contain multiple files, if we sent multicard images or multiple images
# You can download the VCard file, which produced by the recognition method ...
downloaded = email_api.download_file(requests.DownloadFileRequest(
    contact_file.folder_path + '/' + contact_file.file_name,
    storage))
# ... and print it to console
with open(downloaded, 'r') as f:
    file_data = f.read()
    print(file_data)
# Also, you can get VCard object properties’ list using Contact API
contact_properties = email_api.get_contact_properties(
    requests.GetContactPropertiesRequest(
        'VCard',
        contact_file.file_name,
        contact_file.folder_path,
        contact_file.storage))
# All VCard’s properties are available as a list. Complex properties are represented as hierarchical structures.
# Let's print all primitive properties’ values:
primitives = (prop for prop in contact_properties.internal_properties
    if  prop.type == 'PrimitiveObject')
for prop in primitives:
    print('Property name: ' + prop.name + ' value: ' + prop.value)
```
</details>

<details>
    <summary>Parse images directly, without the using of a storage</summary>

```python
# Read image from file and convert it to Base64 string
image_file = 'some/business/card/image/file/on/disk.png'
image_data = None
with open(image_file, 'rb') as f:
    file_data = f.read()
    image_data = str(base64.b64encode(file_data), 'utf-8')
result = email_api.ai_bcr_parse(requests.AiBcrParseRequest(
    models.AiBcrBase64Rq(images=[
        models.AiBcrBase64Image(True, image_data)])))
# Result contains all recognized VCard objects (only the one in our case)
contact_properties = result.value[0]
# VCard object is available as a list of properties, without any external calls:
primitives = (prop for prop in contact_properties.internal_properties
    if  prop.type == 'PrimitiveObject')
for prop in primitives:
    print('Property name: ' + prop.name + ' value: ' + prop.value)
```
</details>

#### Name API
See examples below:
<details open>
    <summary>Detect a person's gender by name</summary>

```python
result = email_api.ai_name_genderize(
    requests.AiNameGenderizeRequest('John Cane'))
# the result contains a list of hypothesis about a person's gender.
# all hypothesis include score, so you can use the most scored version,
# which will be the first in a list:
print(result.value[0].gender) # prints 'Male'
```
</details>

<details>
    <summary>Format person's name using defined format</summary>

```python
result = email_api.ai_name_format(
    requests.AiNameFormatRequest(
        'Mr. John Michael Cane',
        format='%t%L%f%m'))
print(result.name) # prints 'Mr. Cane J. M.'
```
</details>

<details>
    <summary>Compare the names to find out if they belong to the same person or not</summary>

```python
first = 'John Michael Cane'
second = 'Cane J.'
result = email_api.ai_name_match(
    requests.AiNameMatchRequest(first, second))
print(result.similarity >= 0.5) # prints 'True', names look similar
```
</details>

<details>
    <summary>Expand a person's name into a list of possible alternatives</summary>

```python
name = 'Smith Bobby'
result = email_api.ai_name_expand(
    requests.AiNameExpandRequest(name))
expanded_names = list(weighted.name for weighted in result.names)
for (expanded_name in expanded_names):
    print expanded_name # prints 'Mr. Smith', 'B. Smith', etc.
```
</details>

<details>
    <summary>Get k most probable names for given starting characters</summary>

```python
prefix = 'Dav'
result = email_api.ai_name_complete(
    requests.AiNameCompleteRequest(prefix))
names = list(prefix + weighted.name for weighted in result.names)
for (name in names):
    print(name) # prints 'David', 'Dave', 'Davis', etc.
```
</details>

<details>
    <summary>Parse out a person's name from an email address.</summary>

```python
address = 'john-cane@gmail.com'
result = email_api.ai_name_parse_email_address(
    requests.AiNameParseEmailAddressRequest(address))
names = (extracted.name for extracted in result.value)
extracted_values = list(functools.reduce(lambda a,b: a+b, names))
given_name = next((x for x in extracted_values if x.category == 'GivenName'))
surname = next((x for x in extracted_values if x.category == 'Surname'))
print(given_name.value) # prints 'John'
print(surname.value) # prints 'Cane'
```
</details>

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