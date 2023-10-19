import json
from constants import SETTINGS_FILE_NAME

class AppSettings:
    _data = None

    @staticmethod
    def load_settings():
        try:
            with open(SETTINGS_FILE_NAME, 'r') as file:
                AppSettings._data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            AppSettings._data = {}    

    @staticmethod
    def _get_value(key):
        if AppSettings._data == None:
            raise Exception('Error: Configurations Not Loaded')
        return AppSettings._data.get(key)

    @staticmethod
    def get_user_setting(key):
        return AppSettings._get_value('user').get(key)

    @staticmethod
    def get_app_setting(key):
        return AppSettings._get_value('app').get(key)
        
    """
    def set_value(self, key, value):
        if AppSettings._data:
            AppSettings._data[key] = value
            self.save_data()


    def save_data(self):
        with open(SETTINGS_FILE_NAME, 'w') as file:
            json.dump(AppSettings._data, file, indent=4)

    """