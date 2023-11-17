from PyQt5.QtWidgets import QApplication
from Config.app_settings import AppSettings

from sessionScreen import SessionApp

onSession = False
selectedMonitor = 1

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    app = QApplication([])
    window = SessionApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()