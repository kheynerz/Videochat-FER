from app_settings import AppSettings
from session_storage import SessionStorage

from analyze import process_images


def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    #Init UI
    storage = SessionStorage()
    storage.init_session("Test01")
    process_images()

    #End of execution


if __name__ == "__main__":
    main()
    