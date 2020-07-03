import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from conftest import EmailApiData


@pytest.mark.pipeline
def test_file(td: EmailApiData):
    """
    File support test
    """
    sample = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample.ics')
    file_name = str(uuid.uuid4()) + ".ics"
    storage_location = td.folder + "/" + file_name
    td.email.upload_file(requests.UploadFileRequest(storage_location, sample, td.storage))
    downloaded = td.email.download_file(requests.DownloadFileRequest(storage_location, td.storage))
    with open(downloaded, 'r') as f:
        file_data = f.read()
        assert 'Broadway' in file_data


@pytest.mark.pipeline
def test_discover_email_config(td: EmailApiData):
    configs = td.email.discover_email_config(requests.DiscoverEmailConfigRequest('example@gmail.com', True))
    assert len(configs.value) >= 2
    smtp = list(filter(lambda x: x.protocol_type == 'SMTP', configs.value))[0]  # type: models.EmailAccountConfig
    assert smtp.host == 'smtp.gmail.com'


@pytest.mark.pipeline
def test_is_disposable_email(td: EmailApiData):
    disposable = td.email.is_email_address_disposable(
        requests.IsEmailAddressDisposableRequest('example@mailcatch.com'))
    assert disposable.value
    regular = td.email.is_email_address_disposable(
        requests.IsEmailAddressDisposableRequest('example@gmail.com'))
    assert not regular.value


@pytest.mark.pipeline
def test_email_client_account(td: EmailApiData):
    account = models.EmailClientAccount(
        'smtp.gmail.com',
        551,
        'SSLAuto',
        'SMTP',
        models.EmailClientAccountPasswordCredentials(
            'login', None, 'password'))
    name = str(uuid.uuid4()) + '.account'
    td.email.save_email_client_account(
        requests.SaveEmailClientAccountRequest(
            models.StorageFileRqOfEmailClientAccount(
                account, models.StorageFileLocation(
                    td.storage, td.folder, name))))
    result = td.email.get_email_client_account(
        requests.GetEmailClientAccountRequest(
            name, td.folder, td.storage))
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
                                       'example@gmail.com', None, 'password')),
         models.EmailClientAccount('exchange.outlook.com', 443, 'SSLAuto', 'EWS',
                                   models.EmailClientAccountOauthCredentials(
                                       'example@outlook.com', None, 'client_id', 'client_secret', 'refresh_token'))],
        models.EmailClientAccount('smtp.gmail.com', 465, 'SSLAuto', 'SMTP',
                                  models.EmailClientAccountPasswordCredentials(
                                      'example@gmail.com', None, 'password')))
    file_name = str(uuid.uuid4()) + '.multi.account'
    folder = td.folder
    storage = td.storage
    email = td.email
    # Save multi account
    email.save_email_client_multi_account(requests.SaveEmailClientMultiAccountRequest(
        models.StorageFileRqOfEmailClientMultiAccount(
            multi_account,
            models.StorageFileLocation(storage, folder, file_name))))
    # Get multi account object from storage
    multi_account_from_storage = email.get_email_client_multi_account(requests.GetEmailClientMultiAccountRequest(
        file_name, folder, storage))

    assert len(multi_account_from_storage.receive_accounts) == 2
    assert (multi_account_from_storage.send_account.credentials.discriminator ==
            multi_account.send_account.credentials.discriminator)
