from laser import collide
import pygame
import os
import random
from pygame.locals import *
from player import Player
from enemy import Enemy

pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SIZE = (70, 70)
pygame.display.set_caption("The Final Countdown")
# Background
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "background-3.jpg")), (WIDTH, HEIGHT))


def main():
    run = True
    FPS = 60
    level = 1
    enemy_level = 1
    main_font = pygame.font.SysFont("comicsans", 30)
    final_font = pygame.font.SysFont("comicsans", 60)
    player = Player(300, 330, random.choice(["red", "green", "blue"]))
    clock = pygame.time.Clock()
    enemies = []
    wave_length = 1
    player_vel = 3
    enemy_vel = 3
    laser_vel = 9
    victory = False
    victory_count = 0
    lost = False
    lost_count = 0

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
                title_label = main_font.render("Continue", 1, (0, 0, 255))
                WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 450))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_KP_ENTER:
                        run = False
            else:
                continue
        if lost:
            if lost_count == 5:
                title_label = main_font.render("Continue", 1, (0, 0, 255))
                WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 450))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_KP_ENTER:
                        run = False
            else:
                continue

        if len(enemies) == 0:
            for i in range(wave_length):
                enemy = Enemy(400, 50, random.choice(["red", "green", "blue"]))
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
            enemy.move()
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 15) == 1:
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
