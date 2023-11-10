from deepface import DeepFace as df
import concurrent.futures

def calculate_average_emotions(list_of_dictionaries):
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

def analyze(image):
    face_analysis = df.analyze(img_path = f"images/{image}",  actions = ['emotion'], silent=True)
    result = list(map(lambda face: face.get('emotion'), face_analysis))
    #Storage append
    return calculate_average_emotions(result)


def process_images(images):
    results = [None] * len(images)

    # Función para procesar cada imagen individualmente
    def process_image(i):
        result = analyze(images[i])
        results[i] = result

    # Utilizar concurrent.futures para ejecutar las funciones de manera concurrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, range(len(images)))

    return results

if __name__ == "__main__":
    # Supongamos que tienes una lista de imágenes
    images = ['test.png', 'test2.png','test3.png','test4.png']

    # Procesar imágenes concurrentemente y obtener los resultados
    results = process_images(images)

    # Imprimir los resultados (en un orden no determinístico debido a la concurrencia)
    print(results)

