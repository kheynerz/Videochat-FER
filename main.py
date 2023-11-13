from app_settings import AppSettings
from session_storage import SessionStorage

from analyze import process_images

from time import sleep

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    storage = SessionStorage()
    #Init UI (UI Init session)
    storage.init_session("Test01")

    result = process_images()
    #sleep(1)
    #process_images()
    #End of execution


if __name__ == "__main__":
    main()
    