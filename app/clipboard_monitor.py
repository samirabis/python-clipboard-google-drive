import time
import pyperclip
from PIL import ImageGrab
from io import BytesIO


def start_clipboard_monitor(drive_uploader):
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            try:
                im = ImageGrab.grabclipboard()  # get image from clipboard
                if im is not None:
                    byte_data = BytesIO()
                    im.save(byte_data, format="PNG")
                    drive_uploader.upload_file(
                        byte_data.getvalue(), "screenshot.png"
                    )  # upload to google drive
            except Exception as e:
                print(e)  # log the error
        time.sleep(0.1)  # pause to reduce cpu usage
