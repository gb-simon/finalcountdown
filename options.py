
import pygame
import sys
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Videogame')
screen = pygame.display.set_mode((600, 600), 0, 32)
font = pygame.font.SysFont(None, 25)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('About', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press Esc to go back', font,
                  (255, 255, 255), screen, 20, 40)
        draw_text('I made this simple video game ', font,
                  (255, 255, 255), screen, 20, 60)
        draw_text('to get along with python after a time I did not use it.', font,
                  (255, 255, 255), screen, 20, 80)
        draw_text('To win, you have to reach 25 points, ', font,
                  (255, 255, 255), screen, 20, 100)
        draw_text('you can check your score in the inferior side.', font,
                  (255, 255, 255), screen, 20, 120)
        draw_text('To get points you have to move the arrows and avoid the enemies,', font,
                  (255, 255, 255), screen, 20, 140)
        draw_text('each enemy you avoid gives you one point. Good luck, captain.', font,
                  (255, 255, 255), screen, 20, 160)
        draw_text('Made by Gonzalo Simon.', font,
                  (255, 255, 255), screen, 20, 580)

        for event in pygame.event.get():
           
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
