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
    return emotions.get("angry", 0), emotions.get("disgust", 0), emotions.get("fear", 0), emotions.get("happy", 0), emotions.get("sad", 0), emotions.get("surprise", 0), emotions.get("neutral", 0)

notifier = DesktopNotifier()

async def notifierConfig():

    config = read_config()

    silence_alerts = config.get("silentAlerts", False)

    if silence_alerts:
        return

    while True:

        angry, disgust, fear, happy, sad, surprise, neutral = get_emotion_levels()


        for emotion, level in zip(["angry","disgust","fear","happy","sad","surprise","neutral"], [angry,disgust,fear,happy,sad,surprise,neutral]):
            if level >= config.get(emotion, 0):
                n = await notifier.send(title=f"Alerta de {emotion.lower()}", message=f"El {level}% de la clase está {emotion.lower()}.")
                await asyncio.sleep(5)
                await notifier.clear(n)

        time.sleep(config.get("alertRate"))

asyncio.run(notifierConfig())
