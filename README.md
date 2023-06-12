# Python Clipboard to Google Drive Uploader

This Python script continuously monitors the clipboard for new images, and when detected, it automatically uploads them to a specific Google Drive folder.

## Dependencies
This script requires the following Python packages:

- pydrive
- pyperclip
- Pillow

You can install them using pip:

```shell
pip install pydrive pyperclip pillow
```

## Google Drive Setup
Before using this script, you need to set up a `client_secrets.json` file:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the Drive API for your project.
4. Create credentials for a Web application.
5. Download the `client_secrets.json` file.

Move the `client_secrets.json` to the `app` directory.

## Usage
To start the script:

```shell
python app/main.py
```

The script will now start monitoring your clipboard. Whenever you copy an image to your clipboard, it will be automatically uploaded to the specified Google Drive folder.

## License
[MIT](/LICENSE.txt)
