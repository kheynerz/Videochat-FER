import json
from os import makedirs, path
from time import time, sleep

from constants import STORAGE_FOLDER_NAME

from app_settings import AppSettings

class SessionStorage:
    _current_file = None
    _folder_path = None
    _file_counter = 0
    _timestamp = None


    @staticmethod
    def init_session(name : str) -> None: 
        try:
            if not path.exists(STORAGE_FOLDER_NAME):
                makedirs(STORAGE_FOLDER_NAME)
            timestamp = int(time())
            folder_path = path.join(STORAGE_FOLDER_NAME, f"{name}-{timestamp}")
            makedirs(folder_path)
            SessionStorage._folder_path = folder_path
            SessionStorage._create_session_file(timestamp)

        except Exception as e:
            print(f"Error in session creation: {str(e)}")

    @staticmethod
    def _create_session_file(timestamp: int):
        file_name = f"{SessionStorage._file_counter}-{timestamp}"
        SessionStorage._file_counter += 1

        file = open(path.join(SessionStorage._folder_path, file_name), 'wb')
        file.close()
        SessionStorage._current_file = file_name
        SessionStorage._timestamp = timestamp

    @staticmethod
    def check_and_create_file():
        storage = AppSettings()
        STORAGE_CREATION_FILE_RATE = int(storage.get_app_setting('storageCreationFileRate'))

        timestamp = int(time())
        if (timestamp - SessionStorage._timestamp <= STORAGE_CREATION_FILE_RATE) : return
        
        #Calcular promedio del archivo

        SessionStorage._create_session_file(timestamp)


    @staticmethod
    def append_data(data) -> None:
        SessionStorage.check_and_create_file()
      
        current_file = SessionStorage._current_file
        folder_path = SessionStorage._folder_path

        if (current_file == None or folder_path == None): return

        with open(path.join(folder_path, current_file), 'ab') as file:
            data_bytes = f"{json.dumps(data)}\n".encode('utf-8')
            file.write(data_bytes)
            file.close()

