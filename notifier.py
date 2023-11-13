import time
import asyncio
import json
from desktop_notifier import DesktopNotifier

def read_config():
    with open('settings.json', 'r') as f:
        config = json.load(f)
    return config["user"]

def get_emotion_levels():
    with open('emotions.json', 'r') as f:
        emotions = json.load(f)
    return emotions.get("Sadness", 0), emotions.get("Happiness", 0), emotions.get("Boredom", 0), emotions.get("Anger", 0), emotions.get("Excitement", 0), emotions.get("Fear", 0), emotions.get("Surprise", 0)

notifier = DesktopNotifier()

async def notifierConfig():
    # Read the configuration from the JSON file
    config = read_config()

    # Check if alerts are silenced
    silence_alerts = config.get("silentAlerts", False)

    # If alerts are silenced, do nothing else
    if silence_alerts:
        return

    while True:
        # Get the current levels of each emotion
        sadness, happiness, boredom, anger, excitement, fear, surprise = get_emotion_levels()

        # Check each emotion and send the corresponding alerts
        # Only send the alert if the maximum level is a valid number
        for emotion, level in zip(["Sadness", "Happiness", "Boredom", "Anger", "Excitement", "Fear", "Surprise"], [sadness, happiness, boredom, anger, excitement, fear, surprise]):
            if level >= config.get(emotion, 0):
                n = await notifier.send(title=f"Alerta de {emotion.lower()}", message=f"El {level}% de la clase está {emotion.lower()}.")
                await asyncio.sleep(5)
                await notifier.clear(n)

        # Wait 10 seconds before checking again
        time.sleep(10)

# Here you would call the main function
asyncio.run(notifierConfig())
