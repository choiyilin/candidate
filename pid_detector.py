import psutil
import time

def monitor_pids(target_names, on_detect, interval=1.0):
    """
    Poll the OS every `interval` seconds, and call on_detect(pid, name, cmdline)
    the first time we see a matching process (by name or in its command line).
    """
    seen = set()
    targets = [t.lower() for t in target_names]

    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            pid = proc.info['pid']
            name = (proc.info['name'] or '').lower()
            cmdline = ' '.join(proc.info.get('cmdline') or []).lower()

            for target in targets:
                if target in name or target in cmdline:
                    if pid not in seen:
                        seen.add(pid)
                        on_detect(pid, proc.info['name'], proc.info.get('cmdline') or [])
        time.sleep(interval)
