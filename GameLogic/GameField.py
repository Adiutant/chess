import pygame
from random import randint
from GameLogic.Figure import Figure
from GameLogic.King import King
from GameLogic.Queen import Queen
from GameLogic.Pawn import Pawn
from GameLogic.Rook import Rook
from GameLogic.Knight import Knight
from GameLogic.Bishop import Bishop

screenY = 600
screenX = 600
blocknumX = 8
blocknumY = 8
blockSize = screenX / blocknumX
layout = 1  # 0-white
ScreenResolution = (screenX, screenY)
TimeStep = 160
GameField = [
    [9, 7, 11, 5, 3, 11, 7, 9],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [10, 8, 12, 6, 4, 12, 8, 10]
]
RevGameField = [
    [10, 8, 12, 4, 6, 12, 8, 10],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [9, 7, 11, 3, 5, 11, 7, 9]
]
if layout == 0:
    GameField = RevGameField


def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    return res


figures = GameField
GameField = transpose(GameField)
pygame.init()
Screen = pygame.display.set_mode(ScreenResolution)


def setFigure(self):
    if self == 1 or self == 2:
        return Pawn(self)
    if self == 3 or self == 4:
        return King(self)
    if self == 5 or self == 6:
        return Queen(self)
    if self == 7 or self == 8:
        return Knight(self)
    if self == 9 or self == 10:
        return Rook(self)
    if self == 11 or self == 12:
        return Bishop(self)


for i in range(blocknumX):
    for j in range(blocknumY):
        figures[i][j] = setFigure(GameField[i][j])


def drawGrid():
    for x in range(blocknumX):
        for y in range(blocknumY):
            Rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            if (8 - x + 1 + y) % 2 != 0:
                pygame.draw.rect(Screen, (65, 133, 48), Rect, 0)
            else:
                pygame.draw.rect(Screen, (220, 220, 220), Rect, 0)
            try:
                path = figures[x][y].retDrawingSignature()
                if path != 0:
                    image = pygame.image.load('res/' + path)
                    imagex = x * blockSize
                    imagey = y * blockSize
                    direction = 'left'
                    Screen.blit(image, (imagex, imagey))
            except Exception:
                a = 1 + 1


NextMove = pygame.time.get_ticks() + TimeStep
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SpacePressed = True
                while SpacePressed:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_SPACE:
                                SpacePressed = False

    CurrentTime = pygame.time.get_ticks()
    if CurrentTime >= NextMove:
        Screen.fill((220, 220, 220))
        drawGrid()
        pygame.display.update()
        NextMove = pygame.time.get_ticks() + TimeStep
