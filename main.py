from app_settings import AppSettings
from session_storage import SessionStorage


from time import sleep

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    #Init UI
    storage = SessionStorage()
    storage.init_session("CLASE SO HOY")
    
    #End of execution


if __name__ == "__main__":
    main()
    