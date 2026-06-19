import pygame
import random
import os

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

screen_width = int(os.getenv("SCREEN_WIDTH", "900"))
screen_height = int(os.getenv("SCREEN_HEIGHT", "700"))


def shutdown_func(game=True):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = False

        elif event.type == pygame.QUIT:
            game = False

    return game


class Player(pygame.sprite.Sprite):

    def __init__(self, move_up_sound, move_down_sound):

        super(Player, self).__init__()

        self.surf = pygame.image.load("sprites/naruto.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect()

        self.move_up_sound = move_up_sound

        self.move_down_sound = move_down_sound

    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
            self.move_up_sound.play()

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.surf = pygame.image.load("sprites/kunai.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )

        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):

    def __init__(self):

        super(Cloud, self).__init__()

        self.surf = pygame.image.load("sprites/cloud.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # The starting position is randomly generated

        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )

    # Move the cloud based on a constant speed

    # Remove the cloud when it passes the left edge of the screen
    def update(self):

        self.rect.move_ip(-4, 0)

        if self.rect.right < 0:

            self.kill()
