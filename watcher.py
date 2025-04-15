import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.kill()  # Kill old process
        print("Restarting script...")
        self.process = subprocess.Popen(["python", self.script_name])

    def on_modified(self, event):
        if event.src_path.endswith(self.script_name):
            self.start_script()  # Restart script when modified

if __name__ == "__main__":
    script = "lol.py"  # Change this to your script filename
    event_handler = ReloadHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()