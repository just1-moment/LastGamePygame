import pygame
import sys
import os

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Боже, запустись')

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

CURRENT_PATH = os.path.dirname(__file__)
player_image = pygame.image.load(os.path.join(CURRENT_PATH, "image/player.png"))
player_image = pygame.transform.scale(player_image, (100, 100))

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

while True:
    screen.fill(pygame.Color('black'))

    screen.blit(player_image, player_location)

    if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    else:
        pygame.draw.rect(screen, pygame.Color('blue'), test_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(60)