import base64
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
    with open(image_file, 'rb') as f:
        file_data = f.read()
        image_data = str(base64.b64encode(file_data), 'utf-8')
    result = td.api.ai_bcr_parse(requests.AiBcrParseRequest(
        models.AiBcrBase64Rq(
            images=[models.AiBcrBase64Image(True, image_data)])))  # type: models.ListResponseOfHierarchicalObject
    assert len(result.value) == 1
    # noinspection PyTypeChecker
    display_name = list(filter(
        lambda prop: prop.type == 'PrimitiveObject' and prop.name == 'DISPLAYNAME',
        result.value[0].internal_properties))[0]  # type: models.PrimitiveObject
    assert 'Thomas' in display_name.value


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_genderize(td: EmailApiData):
    """ Test name gender detection """
    result = td.api.ai_name_genderize(
        requests.AiNameGenderizeRequest('John Cane'))  # type: models.ListResponseOfAiNameGenderHypothesis
    assert len(result.value) >= 1
    assert result.value[0].gender == 'Male'


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_format(td: EmailApiData):
    result = td.api.ai_name_format(
        requests.AiNameFormatRequest(
            'Mr. John Michael Cane',
            format='%t%L%f%m'))  # type: models.AiNameFormatted
    assert result.name == 'Mr. Cane J. M.'


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_match(td: EmailApiData):
    first = 'John Michael Cane'
    second = 'Cane J.'
    result = td.api.ai_name_match(
        requests.AiNameMatchRequest(first, second))  # type: models.AiNameMatchResult
    assert result.similarity >= 0.5


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_expand(td: EmailApiData):
    name = 'Smith Bobby'
    result = td.api.ai_name_expand(
        requests.AiNameExpandRequest(name))  # type: models.AiNameWeightedVariants
    expanded_names = list(weighted.name for weighted in result.names)
    assert 'Mr. Smith' in expanded_names
    assert 'B. Smith' in expanded_names


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_complete(td: EmailApiData):
    prefix = 'Dav'
    result = td.api.ai_name_complete(
        requests.AiNameCompleteRequest(prefix))  # type: models.AiNameWeightedVariants
    names = list(prefix + weighted.name for weighted in result.names)
    assert 'David' in names
    assert 'Dave' in names
    assert 'Davis' in names


@pytest.mark.ai
@pytest.mark.pipeline
def test_ai_name_parse_email_address(td: EmailApiData):
    address = 'john-cane@gmail.com'
    result = td.api.ai_name_parse_email_address(
        requests.AiNameParseEmailAddressRequest(address))
    names = (extracted.name for extracted in result.value)
    extracted_values = list(functools.reduce(lambda a, b: a + b, names))
    given_name = next((x for x in extracted_values if x.category == 'GivenName'))
    surname = next((x for x in extracted_values if x.category == 'Surname'))
    assert given_name.value == 'John'
    assert surname.value == 'Cane'


@pytest.mark.ai
def test_ai_bcr_parse_model(td: EmailApiData):
    image_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_single_0001.png')
    with open(image_file, 'rb') as f:
        file_data = f.read()
        image_data = str(base64.b64encode(file_data), 'utf-8')
    result = td.api.ai_bcr_parse_model(requests.AiBcrParseModelRequest(
        models.AiBcrBase64Rq(images=[models.AiBcrBase64Image(True, image_data)])))
    assert len(result.value) == 1
    first_vcard = result.value[0]
    assert 'Thomas' in first_vcard.display_name
