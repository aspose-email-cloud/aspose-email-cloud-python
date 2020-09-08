import functools
import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from conftest import EmailApiData


@pytest.mark.ai
def test_ai_bcr_parse_storage(td: EmailApiData):
    file_name = str(uuid.uuid4()) + ".png"
    image_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_single_0001.png')
    # 1) Upload business card image to storage
    storage_location = td.folder + "/" + file_name
    td.api.cloud_storage.file.upload_file(models.UploadFileRequest(storage_location, image_file, td.storage))

    out_folder = str(uuid.uuid4())
    out_folder_path = td.folder + "/" + out_folder
    td.api.cloud_storage.folder.create_folder(models.CreateFolderRequest(out_folder_path, td.storage))
    # 2) Call business card recognition action
    result = td.api.ai.bcr.parse_storage(models.AiBcrParseStorageRequest(
            images=[models.AiBcrImageStorageFile(True, models.StorageFileLocation(td.storage, td.folder, file_name))],
            out_folder=models.StorageFolderLocation(
                td.storage, out_folder_path)))
    # Check that only one file produced
    assert len(result.value) == 1
    # 3) Get file name from recognition result
    contact_file = result.value[0]
    # 4) Download VCard file, produced by recognition method, check it contains text "Thomas"
    downloaded = td.api.cloud_storage.file.download_file(models.DownloadFileRequest(
        contact_file.folder_path + "/" + contact_file.file_name,
        td.storage))
    with open(downloaded, 'r') as f:
        file_data = f.read()
        assert 'Thomas' in file_data


@pytest.mark.ai
def test_ai_bcr_parse(td: EmailApiData):
    image_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_single_0001.png')
    result = td.api.ai.bcr.parse(models.AiBcrParseRequest(image_file))
    assert len(result.value) == 1
    assert 'Thomas' in result.value[0].display_name


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_genderize(td: EmailApiData):
    """ Test name gender detection """
    result = td.api.ai.name.genderize(models.AiNameGenderizeRequest('John Cane'))
    assert len(result.value) >= 1
    assert result.value[0].gender == 'Male'


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_format(td: EmailApiData):
    result = td.api.ai.name.format(models.AiNameFormatRequest('Mr. John Michael Cane', format='%t%L%f%m'))
    assert result.name == 'Mr. Cane J. M.'


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_match(td: EmailApiData):
    first = 'John Michael Cane'
    second = 'Cane J.'
    result = td.api.ai.name.match(models.AiNameMatchRequest(first, second))
    assert result.similarity >= 0.5


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_expand(td: EmailApiData):
    name = 'Smith Bobby'
    result = td.api.ai.name.expand(models.AiNameExpandRequest(name))
    expanded_names = list(weighted.name for weighted in result.names)
    assert 'Mr. Smith' in expanded_names
    assert 'B. Smith' in expanded_names


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_complete(td: EmailApiData):
    prefix = 'Dav'
    result = td.api.ai.name.complete(models.AiNameCompleteRequest(prefix))
    names = list(prefix + weighted.name for weighted in result.names)
    assert 'David' in names
    assert 'Dave' in names
    assert 'Davis' in names


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_parse_email_address(td: EmailApiData):
    address = 'john-cane@gmail.com'
    result = td.api.ai.name.parse_email_address(models.AiNameParseEmailAddressRequest(address))
    names = (extracted.name for extracted in result.value)
    extracted_values = list(functools.reduce(lambda a, b: a + b, names))
    given_name = next((x for x in extracted_values if x.category == 'GivenName'))
    surname = next((x for x in extracted_values if x.category == 'Surname'))
    assert given_name.value == 'John'
    assert surname.value == 'Cane'
