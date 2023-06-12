from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from dotenv import load_dotenv
import os

load_dotenv()


class DriveUploader:
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
        self.drive = GoogleDrive(gauth)

    def upload_file(self, file_data, file_name):
        file = self.drive.CreateFile({"title": file_name})
        file.SetContentString(file_data)
        file.Upload()
