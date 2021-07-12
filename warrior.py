import pygame
import os
from pygame.locals import *
from laser import Laser

pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SIZE = (70, 70)
pygame.display.set_caption("The Final Countdown")

# Load images
RED_WARRIOR = pygame.image.load(
    os.path.join("assets", "red_player.png"))
GREEN_WARRIOR = pygame.image.load(
    os.path.join("assets", "green_player.png"))
BLUE_WARRIOR = pygame.image.load(
    os.path.join("assets", "blue_player.png"))
YELLOW_WARRIOR = pygame.image.load(
    os.path.join("assets", "yellow_player.png"))

class Warrior:
    COOLDOWN = 10

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.warrior_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.vel_x = 1
        self.vel_y = 1

    def draw(self, window):
        window.blit(self.warrior_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 5
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def get_width(self):
        return self.warrior_img.get_width()

    def get_height(self):
        return self.warrior_img.get_height()

    def hit(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
