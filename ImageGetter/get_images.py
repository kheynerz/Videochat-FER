from PIL import ImageGrab
import win32api
import time
from screeninfo import get_monitors
import mss

def capture_full_screen(seconds):
    # # Obtener las dimensiones de la pantalla principal
    # screen_width = win32api.GetSystemMetrics(0)
    # screen_height = win32api.GetSystemMetrics(1)

    # # Captura la pantalla completa
    # img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    
    # # Tiempo antes de tomar la siguiente captura
    # time.sleep(seconds)

    # connected_monitors = get_monitors()
    # for i, screen in enumerate(connected_monitors):
    #     bbox = (screen.x, screen.y, screen.x + screen.width, screen.y + screen.height)
    #     img = ImageGrab.grab(bbox)
    #     img.save(f"screen_{i + 1}.png")

    with mss.mss() as sct:
        captured_monitors = set()
        for i, monitor in enumerate(sct.monitors):
            monitor_id = (
                monitor["width"],
                monitor["height"],
                monitor["left"],
                monitor["top"],
            )
            if monitor_id not in captured_monitors:
                img = sct.shot(output=f"monitor_{i + 1}.png", mon=i)
                captured_monitors.add(monitor_id)
    #return img