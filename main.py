from PyQt5.QtWidgets import QApplication
from Config.app_settings import AppSettings
import os

from sessionScreen import SessionApp

onSession = False
selectedMonitor = 1

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    # Check if the 'images' directory exists, if not, create it
    if not os.path.exists('images'):
        os.makedirs('images')

    app = QApplication([])
    window = SessionApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()