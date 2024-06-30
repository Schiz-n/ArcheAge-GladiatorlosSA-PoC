import time
import os
import pygame
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path, triggers):
        self.file_path = file_path
        self.triggers = triggers
        self.played_lines = set()

    def check_file_for_string(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_lower = line.strip().lower()
                print(line_lower)
                if line_lower not in self.played_lines:
                    self.played_lines.add(line_lower)
                    for target_string, sound_file in self.triggers:
                        if target_string.lower() in line_lower:
                            self.play_sound(sound_file)
                            return True
        return False

    def on_modified(self, event):
        if event.src_path == self.file_path:
            self.check_file_for_string()

    def play_sound(self, sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()

def monitor_file(file_path, triggers):
    # Clear the contents of the file
    open(file_path, 'w').close()
    event_handler = FileChangeHandler(file_path, triggers)
    observer = Observer()
    directory = os.path.dirname(file_path)
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()
    print(f'Started monitoring {file_path}')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    file_to_watch = r"C:\Users\Goliath\Documents\ArcheRage\Misc.log"
    triggers = [
        ("Perry joined the raid.", "Ding.mp3")
    ]
    monitor_file(file_to_watch, triggers)
