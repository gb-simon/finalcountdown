import pygame
import os
from pygame.locals import *
from warrior import Warrior

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


class Player(Warrior):
    COOLDOWN = 27
    COLOR_MAP = {
        "red": (RED_WARRIOR, RED_LASER),
        "green": (GREEN_WARRIOR, GREEN_LASER),
        "blue": (BLUE_WARRIOR, BLUE_LASER),
        "yellow":(YELLOW_WARRIOR, YELLOW_LASER)
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.warrior_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.warrior_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= 10
                        self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y +
                         self.warrior_img.get_height() + 10, self.warrior_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.warrior_img.get_height() +
                         10, self.warrior_img.get_width() * (self.health/self.max_health), 10))
