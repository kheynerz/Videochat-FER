from app_settings import AppSettings
from session_storage import SessionStorage
from ImageGetter.get_images import capture_full_screen

def main() :
    #Load settings
    settings = AppSettings()
    settings.load_settings()
    
    capture_full_screen(2)
    #Init UI
    storage = SessionStorage()
    storage.init_session("Clase de sistemas operativos")
    storage.append_data({"angry": "2%", "happy": "60%"})
    storage.append_data({"angry": "2%", "happy": "60%"})
    storage.append_data({"angry": "2%", "happy": "60%"})


    #End of execution


if __name__ == "__main__":
    main()
    