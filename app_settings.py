import json
from constants import SETTINGS_FILE_NAME

class AppSettings:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        try:
            with open(SETTINGS_FILE_NAME, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}    

    def save_data(self):
        with open(SETTINGS_FILE_NAME, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_value(self, key):
        if self.data:
            return self.data.get(key)

    def set_value(self, key, value):
        if self.data:
            self.data[key] = value
            self.save_data()
