import pygame
import sys
from game import main
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('The Final Countdown')
screen = pygame.display.set_mode((800, 600), 0, 32)
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 35)
BACKGROUND_COLOR = (173, 216, 230)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def warriorSelection():
    click = False
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        yellow = pygame.Rect(50, 100, 200, 50)
        red = pygame.Rect(50, 200, 200, 50)
        blue = pygame.Rect(50, 100, 200, 50)
        green = pygame.Rect(50, 200, 200, 50)
        title = font.render("Select your warrior", True, (0, 0, 0))
        text_1 = font.render("Blue Warrior", True, (0, 100, 190))
        text_2 = font.render("Green Warrior", True, (0, 155, 0))
        text_3 = font.render("Red Warrior", True, (255, 0, 0))
        text_4 = font.render("Yellow Warrior", True, (190, 190, 0))
        help = font.render("With the arrows you move. Press space to attact", True, (0, 0, 0))

        screen.blit(title, (300, 60))
        screen.blit(text_1, (140, 150))
        screen.blit(text_2, (140, 220))
        screen.blit(text_3, (140, 290))
        screen.blit(text_4, (140, 360))
        screen.blit(help, (100, 500))

        pygame.display.flip()

        if blue.collidepoint((mx, my)):
            if click:
                main()
        if green.collidepoint((mx, my)):
            if click:
                main()
        if red.collidepoint((mx, my)):
            if click:
                main()
        if yellow.collidepoint((mx, my)):
            if click:
                main()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
