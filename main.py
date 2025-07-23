import threading
from screenshot_detector import monitor_screenshots
from pid_detector       import monitor_pids
from copy_paste_detector import monitor_copy_and_paste

def on_screenshot(path):
    print(f"🚀 Screenshot detected: {path}")

def on_app_detect(pid, name, cmdline):
    print(f"⚠️  Detected `{name}` (PID {pid})")

def on_copy(text):
    print(f"📋 Copied: {text!r}")

def on_paste(text):
    print(f"📋 Pasted: {text!r}")

def main():
    # 1) Screenshot watcher
    threading.Thread(
        target=monitor_screenshots,
        args=(on_screenshot,),
        daemon=True
    ).start()

    # 2) Copy & paste watcher
    threading.Thread(
        target=monitor_copy_and_paste,
        args=(on_copy, on_paste),
        daemon=True
    ).start()

    # 3) PID watcher (blocks main thread)
    #    Specify the app names to monitor
    #    (case-insensitive).
    print("Hi, welcome to Candidate! This script will monitor your system for screenshots, copy/paste actions, and specific applications.")
    print("Starting PID monitoring...")
    print("Press Ctrl+C to stop.")
    apps_to_flag = [
        "ChatGPT",
        "Claude",
        "Cluely",
        "Xcode",
    ]
    monitor_pids(apps_to_flag, on_app_detect, interval=1.0)

if __name__ == "__main__":
    main()
