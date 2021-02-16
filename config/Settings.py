from domain.Board import *
from service.GameServ import Game
from ui.gui import GUI
from ui.console import *

class Settings:
    def __init__(self, configFile):
        self.__config_file = configFile
        self.__settings = {}

    def readSettings(self):
        with open(self.__config_file, "r") as f:
            lines = f.read().split("\n")
            settings = {}
            for line in lines:
                setting = line.split("=")
                if len(setting) > 1:
                    self.__settings[setting[0].strip()] = setting[1].strip()

    def config(self):
        self.readSettings()
        
        board = None
        computer = None
        game = None
        if self.__settings['repository'] == "in-memory":
            board = Board()
            
        computer = Computer()   
        game = Game(board, computer)    

        ui = None
        if self.__settings['ui'] == "console":
            ui = UI(game)
            
        if self.__settings['ui'] == 'gui':
            ui = GUI(game)
        
        return ui
    
    
        
