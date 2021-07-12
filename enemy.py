import pygame
import os
from pygame.locals import *
from warrior import Warrior
from laser import Laser

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

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))

# scaling image
YELLOW_WARRIOR = pygame.transform.scale(YELLOW_WARRIOR, SIZE)
RED_WARRIOR = pygame.transform.scale(RED_WARRIOR, SIZE)
GREEN_WARRIOR = pygame.transform.scale(GREEN_WARRIOR, SIZE)
BLUE_WARRIOR = pygame.transform.scale(BLUE_WARRIOR, SIZE)
start = True
bounds = pygame.Rect(1, 1, WIDTH, HEIGHT/3)


class Enemy(Warrior):
    COOLDOWN = 10
    COLOR_MAP = {
        "red": (RED_WARRIOR, RED_LASER),
        "green": (GREEN_WARRIOR, GREEN_LASER),
        "blue": (BLUE_WARRIOR, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.warrior_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.warrior_img)
        self.max_health = health

    def move(self):
        if start:
            self.y -= self.vel_y
            self.x -= self.vel_x

        if self.x >= 700 or self.x <= 100:
            self.vel_x *= -1
        if self.x - 10 < bounds.left or self.x + 10 > bounds.right:
            self.vel_x *= -1
        if self.y - 10 < bounds.top or self.y + 10 > bounds.bottom:
            self.vel_y *= -1

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def hit(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y +
                         self.warrior_img.get_height() + 10, self.warrior_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.warrior_img.get_height() +
                         10, self.warrior_img.get_width() * (self.health/self.max_health), 10))
