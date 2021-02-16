from  tkinter import *
import time
import sys
from PIL import Image, ImageTk, ImageOps
from service.GameServ import Game

class GUI:
    def __init__(self, game):
        self._game = game
        self.root = Tk()
        self.root.title('Gomoku')
        self.root.resizable(width = False, height = False) # the main window can't be resized
        self.fgColor = 'red'
        self.bgColor = '#ccccff'
        self.frame = Frame(self.root, bg = self.bgColor)
        self.frame.grid(row = 0, column = 0, sticky="nsew")
        
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        self.root.grid_columnconfigure(1, weight = 1)
        
        self.c = Canvas(self.frame, width = 600, height = 600, borderwidth = 1, bg = self.bgColor)
        self.btnStart = Button(self.frame, text = "Start", bg = self.bgColor, fg = self.fgColor, command = self.start_game)
        self.btnStop = Button(self.frame, text ='Exit', bg = self.bgColor, fg = self.fgColor, command = self.stop_game)
        self.lblMessage = Label(self.frame, bg = self.bgColor, fg = self.fgColor, text = 'Start the game')

        self.c.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        self.lblMessage.grid(row = 1, column = 0, columnspan = 2,  sticky = "nsew")
        self.btnStart.grid(row = 2, column = 0, sticky = "new")
        self.btnStop.grid(row = 2, column = 1, sticky = "new")

        self.ROWS = 15
        self.COLS = 15
        
        self.tiles = [[None for col in range(self.COLS)] for row in range(self.ROWS)]
        self.photoImg = [[None for col in range(self.COLS)] for row in range(self.ROWS)]
        self.c.update()
        self.col_width = self.c.winfo_width() / self.COLS
        self.row_height = self.c.winfo_height() / self.ROWS
        self.c.bind("<Button-1>", self.next_move)
        self.create_table()
        self.player = True
        self.is_running = False;
    @property
    def game(self):
        return self._game
        
    def start(self):
        self.root.mainloop()     
    
    def start_game(self):
        self.lblMessage.configure(text = "Player's move:")
        self.is_running = True
        
    def stop_game(self):
        sys.exit()
               
    def create_table(self):
        width = int(self.col_width)
        height = int(self.row_height)
       
        for row in range(self.ROWS):
            for col in range(self.COLS):
                img = Image.new('RGB', (width, height), (204, 204, 255))
                img = img.resize((width, height), Image.ANTIALIAS)
                self.photoImg[row][col] = ImageTk.PhotoImage(ImageOps.expand(img, border = 1, fill = 'red'))
                self.tiles[row][col] = self.c.create_image(col*self.col_width, row*self.row_height, anchor = NW, image = self.photoImg[row][col])                     
        self.c.update()  
    
    def draw_image(self, row, col, image_file):
        width = int(self.col_width)
        height = int(self.row_height)
       
        self.c.delete(self.photoImg[row][col])
        img = Image.open(image_file).resize((width, height), Image.ANTIALIAS)
        self.photoImg[row][col] = ImageTk.PhotoImage(ImageOps.expand(img, border = 1, fill = 'red'))
        self.c.delete(self.tiles[row][col])
        self.tiles[row][col] = self.c.create_image(col*self.col_width, row*self.row_height, anchor = NW, image = self.photoImg[row][col])
        self.c.update()
        
    def next_move(self, event):
        if self.is_running == False:
            return None
        col = int(event.x//self.col_width)
        row = int(event.y//self.row_height)
        
        if self._game.is_over() == False:     
            self.lblMessage.configure(text = "Computer's move:")
            self.draw_image(row, col, 'resources/x.png')                               
            try:
                self._game.move_player(row, col)
                time.sleep(0.5)
                if self._game.is_over() == True:
                    self.lblMessage.configure(text = 'Game Over: tie or player won')
                    self.is_running = False;
                    return None
            except Exception as e:
                print(e)
                
        if self._game.is_over() == False: 
            (row, col) = self._game.move_computer(row, col)                   
            self.lblMessage.configure(text = "Player's move:")
            self.draw_image(row, col, 'resources/0.png')
            if self._game.is_over() == True:
                self.lblMessage.configure(text = 'Game Over: tie or computer won')
                self.is_running = False;
        return None
            

