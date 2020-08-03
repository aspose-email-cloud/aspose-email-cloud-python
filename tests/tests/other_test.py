import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from conftest import EmailApiData


@pytest.mark.pipeline
def test_file(td: EmailApiData):
    """
    File support test
    """
    sample = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample.ics')
    file_name = str(uuid.uuid4()) + ".ics"
    storage_location = td.folder + "/" + file_name
    td.api.cloud_storage.file.upload_file(models.UploadFileRequest(storage_location, sample, td.storage))
    downloaded = td.api.cloud_storage.file.download_file(models.DownloadFileRequest(storage_location, td.storage))
    with open(downloaded, 'r') as f:
        file_data = f.read()
        assert 'Broadway' in file_data


@pytest.mark.pipeline
def test_discover_email_config(td: EmailApiData):
    configs = td.api.email_config.discover(models.EmailConfigDiscoverRequest('example@gmail.com', True))
    assert len(configs.value) >= 2
    smtp = list(filter(lambda x: x.protocol_type == 'SMTP', configs.value))[0]  # type: models.EmailAccountConfig
    assert smtp.host == 'smtp.gmail.com'


@pytest.mark.pipeline
def test_is_disposable_email(td: EmailApiData):
    disposable = td.api.disposable_email.is_disposable(
        models.DisposableEmailIsDisposableRequest('example@mailcatch.com'))
    assert disposable.value
    regular = td.api.disposable_email.is_disposable(models.DisposableEmailIsDisposableRequest('example@gmail.com'))
    assert not regular.value


@pytest.mark.pipeline
def test_email_client_account(td: EmailApiData):
    account = models.EmailClientAccount(
        'smtp.gmail.com',
        551,
        'SSLAuto',
        'SMTP',
        models.EmailClientAccountPasswordCredentials(
            'login', 'password'))
    name = str(uuid.uuid4()) + '.account'
    td.api.client.account.save(models.EmailClientAccountSaveRequest(
        models.StorageFileLocation(td.storage, td.folder, name),
        account))
    result = td.api.client.account.get(models.ClientAccountGetRequest(name, td.folder, td.storage))
    assert account.host == result.host
    # noinspection PyTypeChecker
    account_credentials = account.credentials  # type: models.EmailClientAccountPasswordCredentials
    # noinspection PyTypeChecker
    result_credentials = result.credentials  # type: models.EmailClientAccountPasswordCredentials
    assert account_credentials.discriminator == result.credentials.discriminator
    assert account_credentials.password == result_credentials.password


@pytest.mark.pipeline
def test_email_client_multi_account(td: EmailApiData):
    # Create multi account object 
    multi_account = models.EmailClientMultiAccount(
        [models.EmailClientAccount('imap.gmail.com', 993, 'SSLAuto', 'IMAP',
                                   models.EmailClientAccountPasswordCredentials(
                                       'example@gmail.com', 'password')),
         models.EmailClientAccount('exchange.outlook.com', 443, 'SSLAuto', 'EWS',
                                   models.EmailClientAccountOauthCredentials(
                                       'example@outlook.com', None, 'client_id', 'client_secret', 'refresh_token'))],
        models.EmailClientAccount('smtp.gmail.com', 465, 'SSLAuto', 'SMTP',
                                  models.EmailClientAccountPasswordCredentials(
                                      'example@gmail.com', 'password')))
    file_name = str(uuid.uuid4()) + '.multi.account'
    # Save multi account
    td.api.client.account.save_multi(models.EmailClientMultiAccountSaveRequest(
        models.StorageFileLocation(td.storage, td.folder, file_name),
        multi_account))
    # Get multi account object from storage
    multi_account_from_storage = td.api.client.account.get_multi(models.ClientAccountGetMultiRequest(
        file_name, td.folder, td.storage))

    assert len(multi_account_from_storage.receive_accounts) == 2
    assert (multi_account_from_storage.send_account.credentials.discriminator ==
            multi_account.send_account.credentials.discriminator)
