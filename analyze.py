import pathlib
from deepface import DeepFace as df
from session_storage import SessionStorage
import os
from app_settings import AppSettings 

def _calculate_average_emotions(list_of_dictionaries):
    settings = AppSettings()
    emotions = settings.get_app_setting('emotions')

    sum_emotions = {emotion: 0 for emotion in emotions}

    for dictionary in list_of_dictionaries:
        if not dictionary: continue
        for emotion, value in dictionary.items():
            sum_emotions[emotion] += value

    number_of_elements = len(list_of_dictionaries)
    average_emotions = {emotion: value / number_of_elements for emotion, value in sum_emotions.items()}

    return average_emotions

def _analyze(image):
    try:
        face_analysis = df.analyze(img_path = f"{image}",  actions = ['emotion'], silent=True)
    except ValueError:
        print(f"faces not found on: {image}")
        return

    result = list(map(lambda face: face.get('emotion'), face_analysis))
    cleaned_result = [valor for valor in result if valor is not None]
    return _calculate_average_emotions(cleaned_result)

def process_images():
    directory = f'{pathlib.Path(__file__).parent.absolute()}/images'
    images = [os.path.join(directory, archivo) for archivo in os.listdir(directory)]
    results = []

    if (len(images) == 0): return
  
    # Función para procesar cada imagen individualmente
    def process_image(i):
        result = _analyze(images[i])
        if (not result): return
        results.append(result)

    for i in range(0, len(images)):
        process_image(i)

    if (len(results) == 0): return
    average_results = _calculate_average_emotions(results)
    SessionStorage.append_data(average_results)

    #for image in images:
    #    os.remove(image)

    return average_results



#Utilizar concurrent.futures para ejecutar las funciones de manera concurrente
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    executor.map(process_image, range(len(images)))