import time
import pyperclip
from PIL import ImageGrab
from io import BytesIO


def start_clipboard_monitor(drive_uploader):
    recent_image = None
    while True:
        try:
            im = ImageGrab.grabclipboard()  # get image from clipboard
            if im is not None and not compare_images(im, recent_image):
                recent_image = im
                byte_data = BytesIO()
                im.save(byte_data, format="PNG")
                drive_uploader.upload_file(
                    byte_data.getvalue(), "screenshot.png"
                )  # upload to google drive
                byte_data.close()  # close the BytesIO object
        except Exception as e:
            print(e)  # log the error
        time.sleep(0.1)  # pause to reduce cpu usage


def compare_images(img1, img2):
    if img1 is None or img2 is None:
        return False
    return list(img1.getdata()) == list(img2.getdata())
