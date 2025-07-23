import time
import threading
import pyperclip
from pynput import keyboard

def monitor_copy(on_copy, interval=0.5):
    """
    Poll the clipboard every `interval` seconds and invoke on_copy(text)
    whenever the clipboard content changes.
    """
    last_text = pyperclip.paste()
    while True:
        try:
            text = pyperclip.paste()
            if text != last_text:
                last_text = text
                on_copy(text)
        except Exception:
            pass
        time.sleep(interval)

def monitor_paste(on_paste):
    """
    Listen for Cmd+V (paste) on macOS and invoke on_paste(text)
    when detected.
    """
    pressed = set()

    def on_press(key):
        pressed.add(key)
        # if Cmd (or Cmd_L/Cmd_R) + 'v' pressed:
        if (keyboard.Key.cmd in pressed or
            keyboard.Key.cmd_l in pressed or
            keyboard.Key.cmd_r in pressed):
            try:
                if key.char.lower() == 'v':
                    text = pyperclip.paste()
                    on_paste(text)
            except AttributeError:
                pass

    def on_release(key):
        pressed.discard(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def monitor_copy_and_paste(on_copy, on_paste, copy_interval=0.5):
    """
    Fire up both monitors in background threads.
    """
    t1 = threading.Thread(target=monitor_copy, args=(on_copy, copy_interval), daemon=True)
    t2 = threading.Thread(target=monitor_paste, args=(on_paste,), daemon=True)
    t1.start()
    t2.start()

    # keep alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

