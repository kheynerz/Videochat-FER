import json
import os
import time

from constants import STORAGE_FOLDER_NAME

class SessionStorage:
    _currentFile = None

    def init_session(self, name : str) -> None: 
        try:
            if not os.path.exists(STORAGE_FOLDER_NAME):
                os.makedirs(STORAGE_FOLDER_NAME)
            
            file_path = os.path.join(STORAGE_FOLDER_NAME, f"{name}-{int(time.time())}.dat")
            open(file_path, 'wb')
            SessionStorage._currentFile = file_path
        except Exception as e:
            print(f"No se pudo crear la sesión: '{STORAGE_FOLDER_NAME}/{name}.dat': {str(e)}")

    def read_from_session(self, start  : str = '0', end : str = f'1000000000') -> None:
        pass

    def append_session(self, data) -> None:
        if (SessionStorage._currentFile == None): return
        with open(SessionStorage._currentFile, 'ab') as file:
            data_with_timestamp = f"{int(time.time())}-{json.dumps(data)}\n"
            data_bytes = data_with_timestamp.encode('utf-8')
            file.write(data_bytes)


