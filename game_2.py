import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SIZE = (70, 70)
pygame.display.set_caption("The Final Countdown")

# Load images
RED_WARRIOR = pygame.image.load(
    os.path.join("assets", "red.png"))
RED_WARRIOR = pygame.image.load(
    os.path.join("assets", "red.png"))
GREEN_WARRIOR = pygame.image.load(
    os.path.join("assets", "green.png"))
BLUE_WARRIOR = pygame.image.load(
    os.path.join("assets", "blue.png"))
YELLOW_WARRIOR = pygame.image.load(
    os.path.join("assets", "yellow.png"))

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


# Background
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "background-3.jpg")), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        # self.y += vel
        pass

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Warrior:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.warrior_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

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
                obj.health -= 10
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

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)


class Player(Warrior):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.warrior_img = YELLOW_WARRIOR
        self.laser_img = YELLOW_LASER
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


class Enemy(Warrior):
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

    def move(self, vel):

        if(self.x <= 50 or self.y <= 50):
            self.x += vel
            self.y += vel
        elif(self.y >= 250):
            self.x -= vel
            self.y -= vel

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


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    FPS = 60
    level = 1
    enemy_level = 1
    main_font = pygame.font.SysFont("comicsans", 30)
    final_font = pygame.font.SysFont("comicsans", 60)
    player_vel = 5
    player = Player(300, 330)
    clock = pygame.time.Clock()
    enemies = []
    wave_length = 1
    enemy_vel = 1
    laser_vel = 5
    lost = False
    lost_count = 0
    victory_count = 0
    victory = False

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # Draw text

        player_level_label = main_font.render(
            f"Your warrior level: {level}", 1, (0, 0, 0))
        WIN.blit(player_level_label,
                 (WIDTH - player_level_label.get_width() - 600, 580))

        enemy_level_label = main_font.render(
            f"Enemy's warrior level: {enemy_level}", 1, (0, 0, 0))
        WIN.blit(enemy_level_label,
                 (WIDTH - enemy_level_label.get_width() - 200, 580))

        kills = main_font.render(
            f"K: {victory_count}", 1, (0, 0, 0))
        WIN.blit(kills, (WIDTH - kills.get_width() - 60, 10))
        deaths = main_font.render(
            f"D: {lost_count}", 1, (0, 0, 0))
        WIN.blit(deaths, (WIDTH - deaths.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if victory:
            victory_label = final_font.render("Victory", 1, (0, 255, 0))
            WIN.blit(victory_label, (WIDTH/2 -
                                     victory_label.get_width()/2, 350))
        if lost:
            lost_label = final_font.render("Defeat", 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if victory:
            if victory_count == 5:
                title_label = main_font.render("Continue", 1, (0,0,255))
                WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 450))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_KP_ENTER:
                        run = False
            else:
                continue
        if lost:
            if lost_count == 5:
                title_label = main_font.render("Continue", 1, (0,0,255))
                WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 450))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_KP_ENTER:
                        run = False
            else:
                continue

        if len(enemies) == 0:
            for i in range(wave_length):
                enemy = Enemy(50, 50, random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.hit()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.hit()

            if collide(enemy, player):
                player.health -= 1
                enemy.health -= 1

            elif enemy.x + enemy.get_width() > WIDTH:
                enemy.x -= enemy_vel

            if enemy.health <= 0:
                victory_count += 1
                level += 1
                enemy.health = 100

            if player.health <= 0:
                lost_count += 1
                enemy_level += 1
                player.health = 100

            if victory_count == 5:
                victory = True
            elif lost_count == 5:
                lost = True

        player.move_lasers(-laser_vel, enemies)


main()
