from domain.Board import *


class Game():
    def __init__(self, board, computer):
        self._board = board
        self._computer = computer

    @property
    def board(self):
        return self._board
    @property
    def computer(self):
        return self._computer

    def move_player(self, x, y):
        self.board.move(x,y,'X')

    def move_computer(self, x, y):

        X,  Y= self.three_in_row(x, y)

        if X == -1 and Y == -1:
            ok = False
            X, Y = self.two_two(x, y)
            if X == -1 and Y ==-1:
                ok = False
                while ok == False:
                    X, Y = self.computer.move_random(x,y)
                    print(X)
                    print(Y)
                    ok = self.board.check2(X,Y)

        self.board.move(X,Y, 'O')
        return (X, Y)

    def three_in_row(self,x,y):
        coordi = [-1, -1, 0, 1, 1, 1, 0, -1]
        coordj = [0, 1, 1, 1, 0, -1, -1, -1]
        for q in range(0, 8):
            ok = True
            xi = x
            yi = y
            for p in range(0, 2):
                xi = xi + coordi[q]
                yi = yi + coordj[q]
                if self.board.onboard(xi, yi) == False:
                    ok = False
                else:
                    if self.board.board[xi][yi] != 1:
                        ok = False
            if ok == True:
                if(self.board.check2(xi+coordi[q],yi+coordj[q])):
                    return xi+coordi[q], yi+coordj[q]
                elif self.board.check2(x-coordi[q], y-coordj[q]):
                    return x-coordi[q], y-coordj[q]
        return -1, -1

    def two_two(self, x, y):
        Xs = -1
        Ys = -1
        coordi = [-1, -1, 0, 1, 1, 1, 0, -1]
        coordj = [0, 1, 1, 1, 0, -1, -1, -1]
        for l in range(0, 8):
            if self.board.board[x+coordi[l]][y+coordj[l]] == 0 and self.board.onboard(x+coordi[l], y+coordj[l]):
                xs = x+coordi[l]
                ys = y+coordj[l]
                for q in range(0, 8):
                    ok = True
                    xi = xs
                    yi = ys
                    xj = xs
                    yj = ys
                    for p in range(0, 1):
                        xi = xi + coordi[q]
                        yi = yi + coordj[q]
                        xj = xj - coordi[q]
                        yj = yj - coordj[q]
                        if self.board.onboard(xi, yi) == False or self.board.onboard(xj, yj) == False:
                            ok = False
                        else:
                            if self.board.board[xi][yi] != 1 or self.board.board[xj][yj] !=1:
                                ok = False
                    if ok == True:
                       Xs = xs
                       Ys = ys

        return Xs, Ys



    def is_won(self):
        ok = self.board.is_won()
        if ok:
            return True
        else:
            return False

    def is_tie(self):
        ok = self.board.is_tie()
        return ok

    def is_over(self):
        return self.board.is_tie() or  self.board.is_won()




