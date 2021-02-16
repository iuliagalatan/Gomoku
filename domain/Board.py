from texttable import *
import random

class Board:

    def __init__(self):
        # 0 - empty square
        # 1 - X
        # -1 - 0
        self._board = [[0 for i in range(15)] for j in range(15)]
        self._moves = 0

    @property
    def moves(self):
        return self._moves

    @property
    def board(self):
        return self._board

    def __str__(self):
        t = Texttable()
        for i in range(15):
            row = list(self.board[i])
            s = {-1: 'O', 0: ' ', 1: 'X'}
            for j in range(15):
                row[j] = s[row[j]]
            t.add_row(row)
        return t.draw()

    def get(self, x, y):
        return self._board[x][y]


    def check(self, x, y):
        if x > 15 or y > 15 or y < 0 or x < 0:
            raise Exception('Out of boundaries')
        if self._board[x][y] != 0:
            raise Exception('Square Taken')
    def onboard(self,x, y):
        if x > 15 or y > 15 or y < 0 or x < 0:
            return False
        return True
    def check2(self,x,y, symbol = 0):
        if x > 15 or y > 15 or y < 0 or x < 0:
            return False
        if self._board[x][y] != symbol:
            return False
        return True
    def move(self, x, y, symbol):
        if symbol not in ['X', 'O']:
            raise Exception('Wrong Symbol')

        self.check(x,y)
        s = {'X':1, 'O':-1}
        self._board[x][y] = s[symbol]
        self._moves+=1

    def is_tie(self):
        if self._moves == 15*15 and self.is_won() == False:
            return True

    def is_won(self, nr = 5):
        a = self._board
        #check horizontally
        for i in range(15):
            s = 0
            l =0
            for j in range(15):
                if a[i][j]== 1:
                    if j == 0:
                        s+=1
                        l+=1
                    elif j != 0 and a[i][j-1] == 1:
                        s+=1
                        l+=1
                    else:
                        if j != 0 and a[i][j-1] == 0:
                            s = 1
                            l = 1
                if s  == nr:
                    return True

        # check vertically
        for j in range(15):
            s = 0
            l = 0
            for i in range(15):
                if a[i][j] == 1:
                    if i == 0:
                        s += 1
                        l += 1
                    elif i != 0 and a[i-1][j] == 1:
                        s += 1
                        l += 1
                    else:
                        if i != 0 and a[i-1][j] == 0:
                            s = 1
                            l = 1
                if s == nr:
                    return True
        #deasupra - principala -check diagonally
        for p in range(0, 5):
            s = 0
            l =0
            last = 0
            for q in range(0,15):
                i = q
                j = i+p
                if j > 14 or j < 0 or i < 0 or i > 14:
                    break
                if a[i][j] == 1:
                    if j == 0:
                        s += 1
                        l += 1
                        last = 1
                    elif j != 0 and last == 1:
                        s += 1
                        l += 1
                        last = 1
                    else:
                        if j != 0 and last == 0:
                            s = 1
                            l = 1
                            last = 1
                else:
                    last = 0
                if s == nr:
                    return True

        # sub - principala -check diagonally
        for p in range(0, 5):
            s = 0
            l = 0
            last =0
            for q in range(0, 15):
                i = q + p
                j = q
                if j > 14 or j < 0 or i < 0 or i > 14:
                    break
                if a[i][j] == 1:
                    if j == 0:
                        s += 1
                        l += 1
                        last = 1
                    elif j != 0 and last == 1:
                        s += 1
                        l += 1
                        last = 1
                    else:
                        if j != 0 and last == 0:
                            s = 1
                            l = 1
                            last = 1
                else:
                    last = 0
                if s == nr:
                    return True
        #sub diag sec
        for p in range(0, 5):
            s = 0
            l =0
            last = 0
            for q in range (0, 15):
                i =q+p
                j =14-q
                if j > 14 or j < 0 or i < 0 or i > 14:
                    break
                if a[i][j] == 1:
                    if j == 0:
                        s += 1
                        l += 1
                        last = 1
                    elif j != 0 and last == 1:
                        s += 1
                        l += 1
                        last = 1
                    else:
                        if j != 0 and last == 0:
                            s = 1
                            l = 1
                            last = 1
                else:
                    last = 0
                if s == nr:
                    return True
        # deasupra diag sec
        for p in range(0, 5):
            s = 0
            l = 0
            last = 0
            for q in range(0, 15):
                i = q
                j = 14 -p-i
                if j > 14 or j < 0 or i < 0 or i > 14:
                    break
                if a[i][j] == 1:
                    if j == 0:
                        s += 1
                        l += 1
                        last = 1
                    elif j != 0 and last == 1:
                        s += 1
                        l += 1
                        last = 1
                    else:
                        if j != 0 and last == 0:
                            s = 1
                            l = 1
                            last = 1
                else:
                    last = 0
                if s == nr:
                    return True
        return False





    def is_lost(self):
        pass


class Computer:
    def move_random(self, x, y):

        coordi = [-1,-1,0,1,1,1,0,-1]
        coordj = [0,1,1,1,0,-1,-1,-1]
        p = random.randint(0, 7)
        return x+coordi[p], y+coordj[p]



'''testing for win works
b =  Board()
b.move(1, 1, 'X')
b.move(2,1,'X')
b.move(3,1,'X')
b.move(4,1,'X')
b.move(5,1,'X')
print(b.is_won())

print(b)

'''
