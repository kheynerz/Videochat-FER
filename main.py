from PyQt5.QtWidgets import QApplication
from Config.app_settings import AppSettings
from Config.session_storage import SessionStorage
from ImageGetter.get_images import capture_full_screen
from analyze import process_images

#from concurrent.futures import ThreadPoolExecutor, wait

from sessionScreen import SessionApp

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

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    app = QApplication([])
    window = SessionApp()
    window.show()
    app.exec_()

    global onSession
    onSession = True

   #In case some images are not processed yet
    process_images()

if __name__ == "__main__":
    main()
   
"""    
with ThreadPoolExecutor() as executor:
    # Ejecutar las funciones concurrentemente
    future_images = executor.submit(getImages)
    future_process = executor.submit(process)
    future_stop = executor.submit(Stop)
    # Esperar a que ambas funciones terminen
    wait([future_images, future_process, future_stop]) 
"""
