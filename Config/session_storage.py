import json
from os import makedirs, path
from time import time

from Config.constants import STORAGE_FOLDER_NAME
from Config.app_settings import AppSettings
from utils import calculate_average_emotions

class SessionStorage:
    _current_file = None
    _folder_path = None
    _file_counter = 0
    _timestamp = None

    _average = []


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

        file = open(path.join(SessionStorage._folder_path, file_name), 'w')
        file.close()

        emotions = {emotion: 0 for emotion in AppSettings.get_app_setting('emotions')}

        emotionsFile = open(path.join(SessionStorage._folder_path, "emotions.json"), 'w')
        emotionsFile.write(json.dumps(emotions))
        emotionsFile.close()

        SessionStorage._current_file = file_name
        SessionStorage._timestamp = timestamp

    @staticmethod
    def _calculate_average(end_timestamp):
        data = []
        with open(path.join(SessionStorage._folder_path, SessionStorage._current_file), 'r') as file:
            fileContent = file.readlines()
            for line in fileContent:
                data.append(json.loads(line)['data'])
        
        folder_path = SessionStorage._folder_path

        if (len(data) == 0): return
        average = calculate_average_emotions(data, AppSettings.get_app_setting('emotions'))
        SessionStorage._average.append(average)

        data_with_timestamp = {"start": SessionStorage._timestamp, "end": end_timestamp, "data": average}
        with open(path.join(folder_path, 'Average.dat'), 'a') as file:
            file.write(f"{json.dumps(data_with_timestamp)}\n")
            file.close()
                
    @staticmethod
    def updateEmotionsFile():
        emotions = AppSettings.get_app_setting('emotions')

        averageData = SessionStorage._average

        emotionsAverage = []
        if (len(averageData) > 0):
            emotionsAverage = calculate_average_emotions(averageData, emotions)
        data = []
        
        with open(path.join(SessionStorage._folder_path, SessionStorage._current_file), 'r') as file:
            fileContent = file.readlines()
            for line in fileContent:
                data.append(json.loads(line)['data'])
        
        data.append(emotionsAverage)

        with open(path.join(SessionStorage._folder_path, "emotions.json"), 'w') as file:
            file.write(json.dumps(calculate_average_emotions(data, emotions)))
            file.close()

    @staticmethod
    def getEmotions():
        emotions = {emotion: 0 for emotion in AppSettings.get_app_setting('emotions')}
        with open(path.join(SessionStorage._folder_path, "emotions.json"), 'r') as file:
            fileContent = file.read()
            emotions = json.loads(fileContent)
            file.close()
        return emotions

    @staticmethod
    def check_and_create_file():
        storage = AppSettings()
        STORAGE_CREATION_FILE_RATE = int(storage.get_app_setting('storageCreationFileRate'))
        timestamp = int(time())
        if (timestamp - SessionStorage._timestamp <= STORAGE_CREATION_FILE_RATE) : return
        
        #Calcular promedio del archivo
        SessionStorage._calculate_average(timestamp)
        SessionStorage._create_session_file(timestamp)

    @staticmethod
    def append_data(data: dict) -> None:
        SessionStorage.check_and_create_file()
        SessionStorage.updateEmotionsFile()

        current_file = SessionStorage._current_file
        folder_path = SessionStorage._folder_path

        if (current_file == None or folder_path == None): return
        data_with_timestamp = {"time": int(time()), "data": data}
        
        with open(path.join(folder_path, current_file), 'a') as file:
            file.write(f"{json.dumps(data_with_timestamp)}\n")
            file.close()
        


