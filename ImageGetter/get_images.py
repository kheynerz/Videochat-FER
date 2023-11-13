import time
import mss
from Config.app_settings import AppSettings

def capture_full_screen(screen_number):
    with mss.mss() as sct:
        for i, _ in enumerate(sct.monitors):
            if(i + 1 == screen_number):
                sct.shot(output=f"images/{int(time.time())}.png", mon=i)

    #Load settings
    settings = AppSettings()
    delay = settings.get_app_setting('screenshotRate')
    time.sleep(delay)
