from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
from dotenv import load_dotenv
import tempfile
import datetime
import time
import os

load_dotenv()


class DriveUploader:
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LoadClientConfigFile(
            "app/client_secrets.json"
        )  # Replace with the full path to your client_secrets.json file
        gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
        self.drive = GoogleDrive(gauth)
        self.folder_id = self.find_or_create_folder("Snippets")
        self.last_temp_file = None

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
        """
        Upload a file to Google Drive.
        :param file_data: The data of the file to be uploaded in bytes.
        :param file_name: The name of the file to be uploaded.
        """

        # Create a temporary file and write the byte data to it
        temp = tempfile.mkstemp(suffix=".png")
        os.close(temp[0])  # Close the file descriptor
        temp_name = temp[1]
        with open(temp_name, "wb") as f:
            f.write(file_data)

        # If there's a previous temp file, attempt to delete it now
        if self.last_temp_file is not None:
            try:
                os.unlink(self.last_temp_file)
                print(
                    f"Previous temporary file {self.last_temp_file} successfully deleted."
                )
            except Exception as e:
                print(
                    f"Failed to delete previous temporary file {self.last_temp_file}: {e}"
                )
            finally:
                self.last_temp_file = None

        # Get the current time and format it as a string
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Use the current time to create a unique file name
        file_name = f"screenshot_{now}.png"

        # Check if folder still exists, if not, create it
        self.folder_id = self.find_or_create_folder("Snippets")

        # Create a new file and set its content
        new_file = self.drive.CreateFile(
            {
                "title": file_name,
                "parents": [{"id": self.folder_id}],
                "mimeType": "image/png",
            }
        )
        new_file.SetContentFile(temp_name)
        new_file.Upload()
        print("File uploaded with ID: ", new_file.get("id"))

        # Instead of deleting the temp file, keep track of it for next time
        self.last_temp_file = temp_name
