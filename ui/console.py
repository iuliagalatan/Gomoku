from service import *
import time

class UI:
    def __init__(self, game):
        self._game = game

    @property
    def game(self):
        return self._game

    def start(self):
        player = True
        while self._game.is_over() == False:
            if player == True:
                x = int(input('coord x: '))
                y = int(input('coord y: '))
                try:
                    self._game.move_player(x,y)
                    player = False
                except Exception as e:
                    print(e)

            else:
                time.sleep(0.5)
                self._game.move_computer(x, y)
                player = True
                print('Computers move:')
            print(self.game.board)
        if player == True:
            print('tie or computer won')
        else:
            print('tie or player won')

