import os
import time
import webbrowser
import json

# TODO: remove class implementation and turn into single "script" file
# TODO: add functionality to join class 5 minutes before


class ZoomLauncher:
    def __init__(self):
        self.time = time.localtime()
        self.today = str(self.time.tm_wday)
        self.hour = str(self.time.tm_hour)
        self.dir = os.path.dirname(__file__)

    def load_schedule(self):
        with open(os.path.join(self.dir, "schedule.json")) as f:
            schedule = json.load(f)
        return schedule[self.today]

    def get_class_url(self):
        schedule = self.load_schedule()
        for class_ in schedule:
            if self.hour in class_.split('-'):
                return schedule[class_]

    def join_class(self):
        url = self.get_class_url()
        if url:
            webbrowser.open(url)
