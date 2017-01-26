from models import Trial
from utils import google_drive


def export_backup(n):
    backup_file = Trial.export_trials(n)
    metadata = {'name': backup_file, 'mimeType': 'application/json'}
    file_resource = google_drive.upload(backup_file, metadata)
    if file_resource:
        Trial.delete_exported_trials()
        return True
    return False
