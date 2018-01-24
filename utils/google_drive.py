import os

import apiclient
import httplib2
from oauth2client import client


def get_credentials():
    return client.GoogleCredentials(
        access_token=os.environ['GOOGLE_DRIVE_ACCESS_TOKEN'],
        client_id=os.environ['GOOGLE_DRIVE_CLIENT_ID'],
        client_secret=os.environ['GOOGLE_DRIVE_CLIENT_SECRET'],
        refresh_token=os.environ['GOOGLE_DRIVE_REFRESH_TOKEN'],
        token_expiry=os.environ['GOOGLE_DRIVE_TOKEN_EXPIRY'],
        token_uri=os.environ['GOOGLE_DRIVE_TOKEN_URI'],
        revoke_uri=os.environ['GOOGLE_DRIVE_REVOKE_URI'],
        user_agent='Python client library'
    )


def initialize_service():
    credentials = get_credentials()
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = apiclient.discovery.build('drive', 'v3', http=http)
    return service


def upload(filename, metadata):
    service = initialize_service()
    files = service.files()
    create_file = files.create(media_body=filename, body=metadata)
    file_resource = create_file.execute()
    return file_resource
