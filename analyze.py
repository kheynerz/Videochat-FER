from deepface import DeepFace as df
from session_storage import SessionStorage
import concurrent.futures
from os import listdir

# Ruta de la carpeta
carpeta = '/ruta/de/tu/carpeta'

# Obtener la lista de archivos en la carpeta

def _calculate_average_emotions(list_of_dictionaries):
    # Initialize a dictionary to store the sum of each emotion
    sum_emotions = {
        'angry': 0,
        'disgust': 0,
        'fear': 0,
        'happy': 0,
        'sad': 0,
        'surprise': 0,
        'neutral': 0
    }

    for dictionary in list_of_dictionaries:
        for emotion, value in dictionary.items():
            sum_emotions[emotion] += value

    number_of_elements = len(list_of_dictionaries)
    average_emotions = {emotion: value / number_of_elements for emotion, value in sum_emotions.items()}

    return average_emotions

def _analyze(image):
    face_analysis = df.analyze(img_path = f"images/{image}",  actions = ['emotion'], silent=True)
    result = list(map(lambda face: face.get('emotion'), face_analysis))
    #Storage append
    return _calculate_average_emotions(result)


def process_images():
    images = listdir('/images')
    print(images)
    results = [None] * len(images)

    # Función para procesar cada imagen individualmente
    def process_image(i):
        result = _analyze(images[i])
        results[i] = result

    # Utilizar concurrent.futures para ejecutar las funciones de manera concurrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, range(len(images)))

    average_results = _calculate_average_emotions(results)
    SessionStorage.append_data(average_results)

    return average_results


