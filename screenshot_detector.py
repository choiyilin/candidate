import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ScreenshotHandler(FileSystemEventHandler):
    """Watches a directory and calls a callback on new screenshot files."""
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def on_created(self, event):
        # Only handle files, not directories
        if event.is_directory:
            return

        filename = os.path.basename(event.src_path).lower()
        # macOS screenshot names contain "screen" or "screenshot" and end in .png
        if filename.endswith(".png") and ("screen" in filename or "screenshot" in filename):
            self.callback(event.src_path)

def get_screenshot_location():
    """
    Returns the directory where macOS saves screenshots, by querying:
      defaults read com.apple.screencapture location
    Falls back to ~/Desktop if that fails.
    """
    try:
        out = subprocess.check_output(
            ["defaults", "read", "com.apple.screencapture", "location"],
            stderr=subprocess.DEVNULL
        )
        path = out.decode().strip()
        if os.path.isdir(path):
            return path
    except Exception:
        pass

    # Fallback
    return os.path.join(os.path.expanduser("~"), "Desktop")

def monitor_screenshots(on_screenshot):
    """
    Start watching the screenshot directory and invoke on_screenshot(path)
    whenever a new screenshot file appears.
    """
    path = get_screenshot_location()
    event_handler = ScreenshotHandler(on_screenshot)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print(f"Watching for screenshots in: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
