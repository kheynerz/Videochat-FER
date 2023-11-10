import time
import mss
from app_settings import AppSettings

def capture_full_screen(screen_number):
    with mss.mss() as sct:
        for i, _ in enumerate(sct.monitors):
            if(i + 1 == screen_number):
                sct.shot(output=f"images/Screen_{i + 1}.png", mon=i)

    #Load settings
    settings = AppSettings()
    settings.load_settings()
    delay = int(settings.get_app_setting('screenshotRate'))
    time.sleep(delay)
