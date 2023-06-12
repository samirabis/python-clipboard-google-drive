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
        self.folder_id = self.find_or_create_folder("Snippets")

    def find_or_create_folder(self, folder_name):
        """Find a folder with the given name, or create it if it doesn't exist."""
        query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        folders = self.drive.ListFile({"q": query}).GetList()
        if len(folders) > 0:
            return folders[0]["id"]  # return the first match
        else:
            # create a new folder
            folder = self.drive.CreateFile(
                {"title": folder_name, "mimeType": "application/vnd.google-apps.folder"}
            )
            folder.Upload()
            return folder["id"]

    def upload_file(self, file_data, file_name):
        file = self.drive.CreateFile(
            {"title": file_name, "parents": [{"id": self.folder_id}]}
        )
        file.SetContentString(file_data)
        file.Upload()
