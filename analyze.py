import pathlib
from time import sleep
from deepface import DeepFace as df
import os

from Config.session_storage import SessionStorage
from Config.app_settings import AppSettings
from utils import calculate_average_emotions 


def _analyze(image):
    settings = AppSettings()
    emotions = settings.get_app_setting('emotions')
    
    try:
        face_analysis = df.analyze(img_path = f"{image}",  actions = ['emotion'], silent=True)
    except ValueError:
        print(f"faces not found on: {image}")
        return

    result = list(map(lambda face: face.get('emotion'), face_analysis))
    cleaned_result = [valor for valor in result if valor is not None]
    return calculate_average_emotions(cleaned_result, emotions)

def process_images():
    directory = os.path.join(pathlib.Path(__file__).parent.absolute(), 'images')
    images = [os.path.join(directory, archivo) for archivo in os.listdir(directory)]
    if (len(images) == 0): return
  
    results = []
    # Función para procesar cada imagen individualmente
    def process_image(image):
        result = _analyze(image)
        if (not result): return
        results.append(result)

    settings = AppSettings()
    emotions = settings.get_app_setting('emotions')
    
    for image in images:
        process_image(image)
        os.remove(image)

    if (len(results) == 0): return
    average_results = calculate_average_emotions(results, emotions)
    SessionStorage.append_data(average_results)
    
    settings = AppSettings()
    delay = settings.get_app_setting('analysisRate')
    sleep(delay)

    return average_results



#Utilizar concurrent.futures para ejecutar las funciones de manera concurrente
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    executor.map(process_image, range(len(images)))