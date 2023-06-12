import os
import threading
from clipboard_monitor import start_clipboard_monitor
from drive_uploader import DriveUploader
from pystray import MenuItem as item, Icon as icon
from PIL import Image

drive_uploader = None  # Declare the drive_uploader at the top-level of your script


def setup(icon):
    global drive_uploader  # Use the global keyword to refer to the global variable
    print("Running setup...")
    image = Image.open(icon_path)
    icon.icon = image
    icon.visible = True
    print("Icon should now be visible...")

    # Start the DriveUploader in a new thread
    uploader_thread = threading.Thread(target=drive_upload, args=(icon,), daemon=True)
    uploader_thread.start()


def drive_upload(icon):
    print("Starting Drive uploader...")
    global drive_uploader
    drive_uploader = DriveUploader()

    # Start the clipboard monitoring in a new thread
    monitor_thread = threading.Thread(
        target=start_clipboard_monitor, args=(drive_uploader,), daemon=True
    )
    monitor_thread.start()


def exit_action(icon, item):
    print("Exiting...")
    icon.stop()


def deauthenticate_action(icon, item):
    print("Deauthenticating...")
    global drive_uploader
    if drive_uploader is not None:
        drive_uploader.deauthenticate()
        print(
            "Deauthentication complete. Please restart the program to authenticate again."
        )
    else:
        print("The Drive uploader has not been initialized yet.")


current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "icon.ico")

print("Starting up...")
menu = (
    item("Deauthenticate", deauthenticate_action),
    item("Exit", exit_action),
)
icon = icon("name", None, "Clipboard Drive", menu)

icon.run(setup)
