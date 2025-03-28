import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("History of Earth")
clock = pygame.time.Clock()
running = True

TITLE_FONT = pygame.font.SysFont("Times New Roman", SCREEN_HEIGHT // 6, bold=True)
PLAY_FONT = pygame.font.SysFont("Arial", SCREEN_HEIGHT // 10, bold=True)
title_surface = TITLE_FONT.render("HISTORY OF EARTH", True, "white")
play_surface = PLAY_FONT.render("PLAY", True, "green")

earth = pygame.image.load("Graphics/Earth.png")
background = pygame.image.load("Graphics/Background.png")

earth1 = pygame.transform.smoothscale(earth, (500, 500))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    screen.blit(background, (0, 0))
    screen.blit(earth1, (180, 200))
    screen.blit(title_surface, (
        SCREEN_WIDTH / 2 - title_surface.get_width() / 2,
        40
    ))
    screen.blit(play_surface, (
        SCREEN_WIDTH * 0.75 - play_surface.get_width() / 2,
        360
    ))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()