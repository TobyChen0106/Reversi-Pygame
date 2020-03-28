from gameBoard import gameBoard
import pygame


class Reversi():
    def __init__(self, size=500, gameName='Reversi'):
        # initial game board
        print('initializing...')
        pygame.init()
        pygame.display.set_caption(gameName)
        self.size = size
        self.screen = pygame.display.set_mode(
            (self.size+self.size//5, self.size+self.size//5*2))

        programIcon = pygame.image.load('Asset/images/icon.jpg')
        pygame.display.set_icon(programIcon)

        self.gameBoard = gameBoard(self.screen, size)

        # locate chess position, 0 for empty, 1 for black chess, -1 for white chess
        self.playingChessColor = 1

        # initial chess positin
        self.gameBoard.setChessPos((3, 3), -1)
        self.gameBoard.setChessPos((3, 4), 1)
        self.gameBoard.setChessPos((4, 3), 1)
        self.gameBoard.setChessPos((4, 4), -1)

    def update(self):
        pos = self.gameBoard.getMouseClick()
        if(pos and not self.gameBoard.getChessPos(pos)):
            if(self.checkFlip(pos, self.playingChessColor)):
                self.gameBoard.setChessPos(pos, self.playingChessColor)
                self.playingChessColor = -1*self.playingChessColor
        return self.gameBoard.update()

    def checkFlip(self, pos, color):
        chessList = self.gameBoard.getChess()
        # check up
        f1 = self.checkDir(chessList, pos, 0, -1, color)
        f2 = self.checkDir(chessList, pos, 0, 1, color)
        f3 = self.checkDir(chessList, pos, 1, -1, color)
        f4 = self.checkDir(chessList, pos, 1, 0, color)
        f5 = self.checkDir(chessList, pos, 1, 1, color)
        f6 = self.checkDir(chessList, pos, -1, -1, color)
        f7 = self.checkDir(chessList, pos, -1, 0, color)
        f8 = self.checkDir(chessList, pos, -1, 1, color)

        return (f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8)

    def checkDir(self, chessList, pos, x_dir, y_dir, color):
        r = pos[0]+y_dir
        c = pos[1]+x_dir
        while(0 <= r <= 7 and 0 <= c <= 7 and chessList[r][c] == -1*color):
            r = r + y_dir
            c = c + x_dir

        if(not (0 <= r <= 7 and 0 <= c <= 7)):
            return False

        if(chessList[r][c] != color or(r == pos[0]+y_dir and c == pos[1]+x_dir)):
            return False

        while(pos[0] != r or pos[1] != c):
            self.gameBoard.setChessPos(pos, color)
            pos = (pos[0]+y_dir, pos[1]+x_dir)
        return True

        # while(r != r_target and c != c_target):
