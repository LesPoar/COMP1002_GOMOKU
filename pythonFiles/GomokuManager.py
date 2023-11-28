import pygame
import math

class GomokuBoard():
    def __init__(self):
        self.Started = False
        self.turn = 0
        self.board = []
        self.dimensions = 1
        self.lastPos = [0,0]
        self.winCon = False
        self.BlackNum = 0 
        self.WhiteNum = 0
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)


    def BoardCreate(self, dimensions):
        self.dimensions = dimensions
        for i in range (dimensions):
            self.board.append([])
            for j in range(dimensions):
                self.board[i].append([])
        self.WhiteNum = dimensions 
        self.BlackNum = dimensions
        self.Started = True
    
    def BoardDraw(self, surface):
        pos = pygame.mouse.get_pos()
        pos_in_board = (pos[0]-50,pos[1]-50)
        posCol = math.floor(pos[1]/(855/self.dimensions))
        posRow = math.floor(pos[0]/(855/self.dimensions))
        
        if(self.Started):
            blocksize = int(855 / self.dimensions)
            self.PlayerDraw(surface)
            self.WinManager()
            for x in range(0,855,blocksize):
                for y in range(0,855,blocksize):
                    rect = pygame.Rect(x+50, y+50, blocksize, blocksize)
                    pygame.draw.rect(surface, pygame.Color("black"), rect, 2)
        if(pygame.mouse.get_pressed()[0]==1 and posRow <= self.dimensions and posRow > 0 and posCol <= self.dimensions and posCol > 0 and self.winCon == False):
            if not self.board[posCol-1][posRow-1] and self.turn % 2 == 0:
                self.board[posCol-1][posRow-1] = 'X'
                self.lastPos[0] = posCol
                self.lastPos[1] = posRow
                self.turn += 1
                self.WhiteNum -= 1
            elif not self.board[posCol-1][posRow-1] and self.turn % 2 == 1:
                self.board[posCol-1][posRow-1] = 'Y'
                self.lastPos[0] = posCol
                self.lastPos[1] = posRow
                self.turn += 1
                self.BlackNum -= 1
                
    def PlayerDraw(self, surface):
            centeringAgent = ((855 / self.dimensions)/2) 
            turn = self.font.render('TURN: ', False, (0, 0, 0))
            surface.blit(turn, (750,920))
            if (self.turn % 2 == 0 and self.winCon == False):
                pygame.draw.circle(surface,(255,255,255),(880,940),20,20)
            elif (self.turn % 2 == 1 and self.winCon == False):
                pygame.draw.circle(surface,(0,0,0),(880,940),20,20)


            for i in range(self.dimensions):
                for j in range(self.dimensions):
                   if self.board[i][j] == 'X':
                       pygame.draw.circle(surface,(255,255,255), (50+centeringAgent+(j*(855/self.dimensions)),50+centeringAgent+(i*(855/self.dimensions))), 20,20)
                   elif self.board[i][j] == 'Y':
                       pygame.draw.circle(surface,(0,0,0), (50+centeringAgent+(j*(855/self.dimensions)),50+centeringAgent+(i*(855/self.dimensions))), 20,20)

    def WinManager(self):
        print(self.turn)
        if(self.DrawCheck()):
            self.winCon = True
            print('Draw')
        elif(self.turn % 2 == 1):
            if(self.RowCheck('X') or self.ColCheck('X') or self.DiagonalCheckLeftToRight('X') or self.DiagonalCheckRightToLeft('X')):
                print('WHITEWIN')
                self.winCon = True
        elif(self.turn % 2 == 0):
            if(self.RowCheck('Y') or self.ColCheck('Y') or self.DiagonalCheckLeftToRight('Y') or self.DiagonalCheckRightToLeft('Y')):
                print('BLACKWIN')
                self.winCon = True

    def DrawCheck(self):
        if (any([] in subl for subl in self.board) and (self.WhiteNum+self.BlackNum) > 0):
            return False
        else:
            return True


    def RowCheck(self,player):
        for row in range(len(self.board[0])):
            for i in range(len(self.board) - 4):
                if self.board[i][row] == self.board[i+2][row] == player and self.board[i+1][row] != player:
                    self.board[i+1][row] = []
                if [self.board[i+j][row] for j in range(5)] == [player]*5:
                    return True
        return False
    def ColCheck(self,player):
        for col in self.board:
            for i in range(len(col) - 4):
                if col[i] == col[i+2] == player and col[i+1] != player:
                    col[i+1] = []
                if col[i:i+5] == [player]*5:
                    return True
        return False
    def DiagonalCheckLeftToRight(self,player):
        for i in range(len(self.board) - 4):
            for j in range(len(self.board[i]) - 4):
                if self.board[i][j] == self.board[i+2][j+2] == player and self.board[i+1][j+1] != player:
                    self.board[i+1][j+1] = []
                if [self.board[i+k][j+k] for k in range(5)] == [player]*5:
                        return True
        return False
    def DiagonalCheckRightToLeft(self,player):
        for i in range(len(self.board) - 4):
            for j in range(4, len(self.board[i])):
                if self.board[i][j] == self.board[i+2][j-2] == player and self.board[i+1][j-1] != player:
                    self.board[i+1][j-1] = []

                if [self.board[i+k][j-k] for k in range(5)] == [player]*5:
                    return True
        return False