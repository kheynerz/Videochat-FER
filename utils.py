def calculate_average_emotions(list_of_dictionaries, emotions):
    sum_emotions = {emotion: 0 for emotion in emotions}

    for dictionary in list_of_dictionaries:
        if not dictionary: continue
        for emotion, value in dictionary.items():
            sum_emotions[emotion] += value

    number_of_elements = len(list_of_dictionaries)
    if number_of_elements == 0: return sum_emotions
    
    average_emotions = {emotion: value / number_of_elements for emotion, value in sum_emotions.items()}

    return average_emotions