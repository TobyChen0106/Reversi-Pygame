import pygame


class gameBoard():
    def __init__(self, screen, size=500):
        # log flags
        self.mouseClickFlag = True
        self.size = size
        self.screen = screen
        # locate chess position, 0 for empty, 1 for black chess, -1 for whilte chess
        self.chess = [[0 for j in range(8)]for i in range(8)]

        self.boardFont = pygame.font.Font(
            "Asset/fonts/Ubuntu-B.ttf", self.size//12)
    
    def getChess(self):
        return self.chess

    def getChessPos(self, pos):
        return self.chess[pos[0]][pos[1]]

    def setChessPos(self, chessPos, chessColor=0):
        self.chess[chessPos[0]][chessPos[1]] = chessColor

    def getMouseClick(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if(click[0] and self.mouseClickFlag):
            self.mouseClickFlag = False
            if (self.size//10 <= mouse[0] <= self.size//10+self.size and self.size//10 <= mouse[1] <= self.size//10+self.size):
                return ((mouse[1]-self.size//10-self.size//200)//(self.size//8), (mouse[0]-self.size//10-self.size//200)//(self.size//8))
        if(not click[0]):
            self.mouseClickFlag = True
        return None

    def update(self):
        self.screen.fill((0, 0, 0))
        self.drawBoard()
        self.drawChess()
        self.drawPoints()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def drawBoard(self):
        self.screen.fill((0x08, 0x40, 0x56))
        pygame.draw.rect(self.screen, (0x18, 0x83, 0x67),
                         (self.size//10, self.size//10, self.size, self.size))

        VerticalCoordinateText = ['1', '2', '3', '4', '5', '6', '7', '8']
        HorizontalCoordinateText = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        for index, t in enumerate(VerticalCoordinateText):
            text_surface = self.boardFont.render(t, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.size//40,
                                            self.size//9 + self.size//8*index))
        for index, t in enumerate(HorizontalCoordinateText):
            text_surface = self.boardFont.render(t, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.size//10 +
                                            self.size//30 + self.size//8*index, 0))
        for i in range(9):
            pygame.draw.rect(self.screen, (0x4E, 0x6B, 0x5C),
                             (self.size//10+i*self.size//8, self.size//10, self.size//100, self.size+self.size//100))
            pygame.draw.rect(self.screen, (0x4E, 0x6B, 0x5C),
                             (self.size//10, self.size//10+i*self.size//8, self.size+self.size//100, self.size//100))

    def drawChess(self):
        for colIndex in range(8):
            for rowIndex in range(8):
                if(self.chess[rowIndex][colIndex] == 1):
                    pygame.draw.circle(self.screen, (25, 25, 25), (self.size//10 + self.size//16 + self.size//200 + self.size//8*colIndex, self.size//10 + self.size//16 + self.size//200 +
                                                                   self.size//8*rowIndex), self.size//20)
                    pygame.draw.circle(self.screen, (0, 0, 0), (self.size//10 + self.size//16 + self.size//200 + self.size//8*colIndex, self.size//10 + self.size//16 + self.size//200 +
                                                                self.size//8*rowIndex), self.size//25)
                elif(self.chess[rowIndex][colIndex] == -1):
                    pygame.draw.circle(self.screen, (255, 255, 255), (self.size//10 + self.size//16 + self.size//200 + self.size//8*colIndex, self.size//10 + self.size//16 + self.size//200 +
                                                                      self.size//8*rowIndex), self.size//20)
                    pygame.draw.circle(self.screen, (220, 220, 220), (self.size//10 + self.size//16 + self.size//200 + self.size//8*colIndex, self.size//10 + self.size//16 + self.size//200 +
                                                                      self.size//8*rowIndex), self.size//25)
                    

    def drawPoints(self):
        blackSum = 0
        whiteSum = 0
        for colIndex in range(8):
            for rowIndex in range(8):
                if(self.chess[rowIndex][colIndex] == 1):
                    blackSum += 1
                elif(self.chess[rowIndex][colIndex] == -1):
                    whiteSum += 1
        # draw black chess
        pygame.draw.circle(self.screen, (25, 25, 25), (self.size//10 + self.size //
                                                       4, self.size//10+self.size//100+self.size//20+self.size), self.size//30)
        pygame.draw.circle(self.screen,  (0, 0, 0), (self.size//10 + self.size //
                                                     4, self.size//10+self.size//100+self.size//20+self.size), self.size//35)
        text_surface = self.boardFont.render(
            str(blackSum), True, (255, 255, 255))
        self.screen.blit(text_surface, (self.size//10 + self.size //
                                        4 + self.size//16, self.size//10+self.size//100+self.size))

        # draw white chess
        pygame.draw.circle(self.screen, (255, 255, 255), (self.size//10 + self.size //
                                                          4*3, self.size//10+self.size//100+self.size//20+self.size), self.size//30)
        pygame.draw.circle(self.screen, (220, 220, 220), (self.size//10 + self.size //
                                                          4*3, self.size//10+self.size//100+self.size//20+self.size), self.size//35)
        text_surface = self.boardFont.render(
            str(whiteSum), True, (255, 255, 255))
        self.screen.blit(text_surface, (self.size//10 + self.size //
                                        4*3 - self.size//16-text_surface.get_rect().width, self.size//10+self.size//100+self.size))