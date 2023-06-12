import os
from clipboard_monitor import start_clipboard_monitor
from drive_uploader import DriveUploader
from pystray import MenuItem as item, Icon as icon
from PIL import Image


def setup(icon, drive_uploader):
    icon.visible = True
    start_clipboard_monitor(drive_uploader)


def exit_action(icon, item):
    icon.stop()


current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "icon.png")
image = Image.open(icon_path)

drive_uploader = DriveUploader()
menu = (item("Exit", exit_action),)
icon = icon("name", image, "My System Tray Icon", menu)
icon.run(setup(icon, drive_uploader))
