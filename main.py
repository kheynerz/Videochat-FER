
from Config.app_settings import AppSettings
from Config.session_storage import SessionStorage
from ImageGetter.get_images import capture_full_screen
from analyze import process_images

from concurrent.futures import ThreadPoolExecutor, wait

from time import sleep

onSession = False

selectedMonitor = 1

def getImages(): 
    global onSession
    while (onSession):
        capture_full_screen(selectedMonitor)

def process():
    global onSession
    while (onSession):
        process_images()

def Stop():
    global onSession
    sleep(10)
    onSession = False

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    storage = SessionStorage()
    #Init UI (UI Init session)
    storage.init_session("Test03")

    global onSession
    onSession = True

    with ThreadPoolExecutor() as executor:
        # Ejecutar las funciones concurrentemente
        future_images = executor.submit(getImages)
        future_process = executor.submit(process)
        future_stop = executor.submit(Stop)
        # Esperar a que ambas funciones terminen
        wait([future_images, future_process, future_stop])
   
   #In case some images are not processed yet
    process_images()

if __name__ == "__main__":
    main()
   