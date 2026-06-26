#!/usr/bin/env python3
# Here are we start again!
import random

import pygame.sprite
import pygame.font

from game_classes import *


def draw_menu(screen, font, cloud_surf, naruto_surf, mouse_pos):
    screen.fill((135, 206, 250))
    title = font.render("NarutoCloudBattle", True, (255, 255, 255))
    title_x = screen_width//2 - title.get_width()//2
    naruto_before_x = title_x - 60
    screen.blit(naruto_surf, (naruto_before_x, 100))
    screen.blit(title, (title_x, 100))
    naruto_after_x = title_x + title.get_width() + 10
    screen.blit(naruto_surf, (naruto_after_x, 100))

    start_button = pygame.Rect(screen_width//2 - 100, 200, 200, 50)
    screen.blit(cloud_surf, (start_button.x, start_button.y))
    start_color = (255, 255, 0) if start_button.collidepoint(mouse_pos) else (0, 0, 0)
    start_text = font.render("Start", True, start_color)
    screen.blit(start_text, (start_button.centerx - start_text.get_width()//2, start_button.centery - start_text.get_height()//2))

    exit_button = pygame.Rect(screen_width//2 - 100, 300, 200, 50)
    screen.blit(cloud_surf, (exit_button.x, exit_button.y))
    exit_color = (255, 255, 0) if exit_button.collidepoint(mouse_pos) else (0, 0, 0)
    exit_text = font.render("Exit", True, exit_color)
    screen.blit(exit_text, (exit_button.centerx - exit_text.get_width()//2, exit_button.centery - exit_text.get_height()//2))

    return start_button, exit_button

def draw_game_over_menu(screen, font, cloud_surf, kunai_surf, mouse_pos):
    screen.fill((135, 206, 250))
    title = font.render("Game Over", True, (255, 0, 0))
    title_x = screen_width//2 - title.get_width()//2
    kunai_before_x = title_x - 60
    screen.blit(kunai_surf, (kunai_before_x, 100))
    screen.blit(title, (title_x, 100))
    kunai_after_x = title_x + title.get_width() + 10
    screen.blit(kunai_surf, (kunai_after_x, 100))

    restart_button = pygame.Rect(screen_width//2 - 100, 200, 200, 50)
    screen.blit(cloud_surf, (restart_button.x, restart_button.y))
    restart_color = (255, 255, 0) if restart_button.collidepoint(mouse_pos) else (0, 0, 0)
    restart_text = font.render("Restart", True, restart_color)
    screen.blit(restart_text, (restart_button.centerx - restart_text.get_width()//2, restart_button.centery - restart_text.get_height()//2))

    exit_button = pygame.Rect(screen_width//2 - 100, 300, 200, 50)
    screen.blit(cloud_surf, (exit_button.x, exit_button.y))
    exit_color = (255, 255, 0) if exit_button.collidepoint(mouse_pos) else (0, 0, 0)
    exit_text = font.render("Exit", True, exit_color)
    screen.blit(exit_text, (exit_button.centerx - exit_text.get_width()//2, exit_button.centery - exit_text.get_height()//2))

    return restart_button, exit_button

def main():

    pygame.mixer.init()

    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    pygame.mixer.music.load("sprites/Naruto_Theme.mp3")

    pygame.mixer.music.play(loops=-1)

    move_right_sound = pygame.mixer.Sound("sprites/jumping.wav")

    move_left_sound = pygame.mixer.Sound("sprites/jumping.wav")

    collision_sound = pygame.mixer.Sound("sprites/hit.wav")

    enemies = pygame.sprite.Group()

    clouds = pygame.sprite.Group()
    # Define constants for the screen width and height
    screen = pygame.display.set_mode([screen_width, screen_height])
    cloud_surf = pygame.image.load("sprites/cloud.png").convert()
    cloud_surf.set_colorkey((0, 0, 0), RLEACCEL)
    cloud_surf = pygame.transform.scale(cloud_surf, (200, 50))
    naruto_surf = pygame.image.load("sprites/naruto.png").convert()
    naruto_surf.set_colorkey((0, 0, 0), RLEACCEL)
    naruto_surf = pygame.transform.scale(naruto_surf, (50, 50))
    kunai_surf = pygame.image.load("sprites/kunai.png").convert()
    kunai_surf.set_colorkey((0, 0, 0), RLEACCEL)
    kunai_surf = pygame.transform.scale(kunai_surf, (50, 50))
    heart_surf = pygame.image.load("sprites/heart.png").convert()
    heart_surf.set_colorkey((255, 255, 255), RLEACCEL)
    heart_surf = pygame.transform.scale(heart_surf, (30, 30))
    player_1 = Player()

    all_sprites_upper = pygame.sprite.Group()
    all_sprites_lower = pygame.sprite.Group()

    # Create a custom event for adding a new enemy

    ADDENEMY = pygame.USEREVENT + 1

    pygame.time.set_timer(ADDENEMY, 500)

    ADDECLOUD = pygame.USEREVENT + 2

    pygame.time.set_timer(ADDECLOUD, 1000)

    game_state = 'menu'
    game_on = True
    lives = 3
    invincible = False
    invincible_timer = 0
    start_button = None
    restart_button = None
    exit_button = None
    while game_on:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_on = False
                if game_state == 'playing':
                    if event.key == K_RIGHT:
                        move_right_sound.play()
                    elif event.key == K_LEFT:
                        move_left_sound.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game_state == 'menu' and start_button and start_button.collidepoint(mouse_pos):
                    game_state = 'playing'
                    player_1 = Player()
                    enemies.empty()
                    clouds.empty()
                    all_sprites_upper.empty()
                    all_sprites_lower.empty()
                    lives = 3
                    invincible = False
                    invincible_timer = 0
                elif game_state == 'game_over' and restart_button and restart_button.collidepoint(mouse_pos):
                    game_state = 'playing'
                    player_1 = Player()
                    enemies.empty()
                    clouds.empty()
                    all_sprites_upper.empty()
                    all_sprites_lower.empty()
                    lives = 3
                    invincible = False
                    invincible_timer = 0
                elif exit_button and exit_button.collidepoint(mouse_pos):
                    game_on = False

            if game_state == 'playing':
                if event.type == ADDENEMY:
                    # Create the new enemy and add it to sprite groups

                    new_enemy = Enemy()

                    enemies.add(new_enemy)

                    all_sprites_upper.add(new_enemy)

                elif event.type == ADDECLOUD:
                    # Create the new enemy and add it to sprite groups

                    new_cloud = Cloud()

                    clouds.add(new_cloud)

                    if random.randint(0, 3) == 0:
                        all_sprites_upper.add(new_cloud)
                    else:
                        all_sprites_lower.add(new_cloud)

        if game_state == 'playing':
            pressed_keys = pygame.key.get_pressed()

            player_1.update(pressed_keys)

            enemies.update()
            clouds.update()

            if invincible:
                invincible_timer -= 1
                if invincible_timer <= 0:
                    invincible = False

            screen.fill((135, 206, 250))

            for entity in all_sprites_lower:
                screen.blit(entity.surf, entity.rect)

            if not invincible or invincible_timer % 4 < 2:
                screen.blit(player_1.surf, player_1.rect)

            for entity in all_sprites_upper:
                screen.blit(entity.surf, entity.rect)

            for i in range(lives):
                x = screen_width - (i + 1) * (30 + 10)
                screen.blit(heart_surf, (x, 10))

            if pygame.sprite.spritecollideany(player_1, enemies):
                if not invincible:
                    lives -= 1
                    invincible = True
                    invincible_timer = 60
                    collision_sound.play()
                    hit_enemy = pygame.sprite.spritecollideany(player_1, enemies)
                    if hit_enemy:
                        hit_enemy.kill()
                    if lives <= 0:
                        game_state = 'game_over'
                        player_1.kill()
                        move_right_sound.stop()
                        move_left_sound.stop()

        elif game_state == 'menu':
            start_button, exit_button = draw_menu(screen, font, cloud_surf, naruto_surf, mouse_pos)

        elif game_state == 'game_over':
            restart_button, exit_button = draw_game_over_menu(screen, font, cloud_surf, kunai_surf, mouse_pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

    # Ensure program maintains a rate of 30 frames per second


if __name__ == "__main__":
    main()
