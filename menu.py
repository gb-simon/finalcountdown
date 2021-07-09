
from game import *
import sys
from options import *
import pygame
import sys

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Videogame')
screen = pygame.display.set_mode((600, 600), 0, 32)
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None,35)
BACKGROUND_COLOR = (173, 216, 230)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill(BACKGROUND_COLOR)
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        text_1 = font.render("Start", True, (0,0,0))
        text_2 = font.render("About", True, (0,0,0))

        screen.blit(text_1, (140, 120))
        screen.blit(text_2, (140, 220))

        pygame.display.flip()
       

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()
