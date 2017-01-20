import json
from oauth2client import client, file, tools


STORAGE = '/tmp/storage'
ENVIRONMENT_FORMAT = '/tmp/credentials.env'
CLIENT_SECRET_FILE = '/tmp/client_secret.json'
SCOPES = 'https://www.googleapis.com/auth/drive'


def get_from_google():
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    store = file.Storage(STORAGE)
    tools.run_flow(flow, store)


def export_to_env_format():
    with open(STORAGE) as input_file:
        cred = json.load(input_file)
    credentials = [
        'GOOGLE_DRIVE_ACCESS_TOKEN=' + cred['access_token'] + '\n',
        'GOOGLE_DRIVE_CLIENT_ID=' + cred['client_id'] + '\n',
        'GOOGLE_DRIVE_CLIENT_SECRET=' + cred['client_secret'] + '\n',
        'GOOGLE_DRIVE_REFRESH_TOKEN=' + cred['refresh_token'] + '\n',
        'GOOGLE_DRIVE_TOKEN_EXPIRY=' + cred['token_expiry'] + '\n',
        'GOOGLE_DRIVE_TOKEN_URI=' + cred['token_uri'] + '\n',
        'GOOGLE_DRIVE_REVOKE_URI=' + cred['revoke_uri'] + '\n'
    ]
    with open(ENVIRONMENT_FORMAT, 'w') as output_file:
        output_file.writelines(credentials)


if __name__ == '__main__':
    get_from_google()
    export_to_env_format()
