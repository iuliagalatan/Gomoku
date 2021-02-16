from config.Settings import Settings

class App:
    '''
        main class which initialize the entire app
    '''
    @staticmethod
    def start():
        settings = Settings("settings.properties")
        ui = settings.config()
        ui.start()


App.start()
