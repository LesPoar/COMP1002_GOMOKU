import pygame
import button
import GomokuManager as gm

screen = pygame.display.set_mode((1000,1000))

pygame.display.set_caption('Gomoku COMP1002')

img15 = pygame.image.load('15x15.png').convert_alpha()
img19 = pygame.image.load('19x19.png').convert_alpha()

button15 = button.Button(100,920,img15,1)
button19 = button.Button(400,920,img19,1)

game = gm.GomokuBoard()

gamestart = False
run =True
dimensions = 0

while run:
    screen.fill((215,179,119))
    if button15.draw(screen) and gamestart == False:
        game.BoardCreate(15)
        gamestart = True
    if button19.draw(screen) and gamestart == False:
        game.BoardCreate(19)
        gamestart = True

    game.BoardDraw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()