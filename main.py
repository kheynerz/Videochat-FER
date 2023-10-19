from app_settings import AppSettings

def main() :
    #Load settings
    settings = AppSettings()
    user_settings = settings.get_value('user')
    app_settings = settings.get_value('app')

    #Init UI


    #End of execution

    pass


if __name__ == "__main__":
    main()
    