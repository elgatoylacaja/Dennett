import json
from utils import google_drive


def download_from_mongo():
    filename = 'foo.json'
    data = {'foo': 'bar'}
    with open(filename, 'w') as outfile:
        json.dump(data, outfile) 
    return filename 


def delete_from_mongo():
    pass


def backup():
    backup_file = download_from_mongo()
    metadata = {'name': backup_file, 'mimeType': 'application/json'}
    file_resource = google_drive.upload(backup_file, metadata)
    if file_resource:
        delete_from_mongo()
        return True
    return False
