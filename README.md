# Python Clipboard to Google Drive Uploader

This Python script continuously monitors the clipboard for new images, and when detected, it automatically uploads them to a specified Google Drive folder. It also provides a system tray icon for easy access to functionalities such as exiting the program and deauthentication.

## Dependencies
This script requires the following Python packages:

- pydrive
- pyperclip
- Pillow
- pystray

You can install them using pip:

```shell
pip install pydrive pyperclip pillow pystray
```

## Google Drive Setup
Before using this script, you need to set up a `client_secrets.json` file:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the Drive API for your project.
4. Create credentials for a Web application.
5. Download the `client_secrets.json` file.

Move the `client_secrets.json` file to the `app` directory.

## Usage
To start the script:

```shell
python app/main.py
```

The script will now start monitoring your clipboard. Whenever you copy an image to your clipboard, it will be automatically uploaded to the specified Google Drive folder. An icon will be available in the system tray. From the icon, you can exit the program or deauthenticate your Google account to change the Drive where images are uploaded.

## Authentication
On the first run, the application will open a web page for you to grant it access to your Google Drive. This authentication process is required only once as the token is stored locally for future use.

If you wish to change the Google account or remove access, you can deauthenticate by right-clicking on the system tray icon and selecting 'Deauthenticate'. 

## License
[MIT](/LICENSE.txt)
