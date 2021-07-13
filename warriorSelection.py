from enemy import HEIGHT, WIDTH
import pygame
import sys
from game import main
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('The Final Countdown')
screen = pygame.display.set_mode((800, 600), 0, 32)
WHITE = (255, 255, 255)
title_font = pygame.font.SysFont(None, 35)
warrior_font = pygame.font.SysFont(None, 15)
normal_font = pygame.font.SysFont(None, 25)
BACKGROUND_COLOR = (173, 216, 230)
square_size_x, square_size_y = 75, 75

# Colors
blue_color = (0, 0, 255)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
yellow_color = (255, 255, 0)

def draw_text(text, normal_font, color, surface, x, y):
    textobj = normal_font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def warriorSelection():
    click = False
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_text('main menu', normal_font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()

        blue = pygame.Rect(200, 150, square_size_x, square_size_y)
        green = pygame.Rect(300, 150, square_size_x, square_size_y)
        red = pygame.Rect(400, 150, square_size_x, square_size_y)
        yellow = pygame.Rect(500, 150, square_size_x, square_size_y)

        title = title_font.render("Select your warrior", True, (0, 0, 0))
        text_1 = warrior_font.render("Axel", True, (0, 100, 190))
        text_2 = warrior_font.render("Letage", True, (0, 155, 0))
        text_3 = warrior_font.render("Horo", True, (255, 0, 0))
        text_4 = warrior_font.render("Ignatius", True, (190, 190, 0))
        help = normal_font.render("With the arrows you move. Press space to attact", True, (0, 0, 0))
        
        pygame.draw.rect(screen, blue_color, blue)
        pygame.draw.rect(screen, green_color, green)
        pygame.draw.rect(screen, red_color, red)
        pygame.draw.rect(screen, yellow_color, yellow)

        screen.blit(title, (300, 60))
        screen.blit(text_1, (210, 250))
        screen.blit(text_2, (310, 250))
        screen.blit(text_3, (410, 250))
        screen.blit(text_4, (510, 250))
        screen.blit(help, (100, 500))


        if blue.collidepoint((mx, my)):
            print("ready for the party")
            if click:
                main("blue")
        if green.collidepoint((mx, my)):
            if click:
                print("NACHOOO")
                main("green")
        if red.collidepoint((mx, my)):
            print("dejame el red")
            if click:
                main("red")
        if yellow.collidepoint((mx, my)):
            print("ya está, yo estoy en bata")
            if click:
                main("yellow")

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
