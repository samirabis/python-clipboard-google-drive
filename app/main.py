from app.clipboard_monitor import start_clipboard_monitor
from app.drive_uploader import DriveUploader
from pystray import MenuItem as item, Icon as icon
from PIL import Image


def setup(icon, drive_uploader):
    icon.visible = True
    start_clipboard_monitor(drive_uploader)


def exit_action(icon, item):
    icon.stop()


image = Image.open("icon.png")  # icon.png is the system tray icon
drive_uploader = DriveUploader()
menu = (item("Exit", exit_action),)
icon = icon("name", image, "My System Tray Icon", menu)
icon.run(setup(icon, drive_uploader))
