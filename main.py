import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("History of Earth")
clock = pygame.time.Clock()
room = 1
mya_counter = 5400
running = True

YRS_FONT = pygame.font.SysFont("Times New Roman", SCREEN_HEIGHT // 16, bold=True)
TITLE_FONT = pygame.font.SysFont("Times New Roman", SCREEN_HEIGHT // 6, bold=True)
PLAY_FONT = pygame.font.SysFont("Arial", SCREEN_HEIGHT // 10, bold=True)
title_surface = TITLE_FONT.render("HISTORY OF EARTH", True, "white")
play_surface = PLAY_FONT.render("PLAY", True, "green")
yrs_surface = YRS_FONT.render(f"{mya_counter} MYA", True, "orange")
play_surface_pos = (
    SCREEN_WIDTH * 0.75 - play_surface.get_width() / 2,
    360
)

earth = pygame.image.load("Graphics/Earth.png")
hadean_earth = pygame.image.load("Graphics/hadean_earth.png")
sun = pygame.image.load("Graphics/Sun.png")
background = pygame.image.load("Graphics/Background.png")

earth1 = pygame.transform.smoothscale(earth, (500, 500))
hadean_earth1 = pygame.transform.smoothscale(hadean_earth, (500, 500))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if room == 0 and (
                event.pos[0] > play_surface_pos[0] and
                event.pos[1] > play_surface_pos[1] and
                event.pos[0] < play_surface_pos[0] + play_surface.get_width() and
                event.pos[1] < play_surface_pos[1] + play_surface.get_height()
            ):
                room = 1


    screen.fill("black")

    if room == 0:
        screen.blit(background, (0, 0))
        screen.blit(earth1, (180, 200))
        screen.blit(title_surface, (
            SCREEN_WIDTH / 2 - title_surface.get_width() / 2,
            40
        ))
        screen.blit(play_surface, play_surface_pos)
    elif room == 1:
        screen.blit(sun, (640, 360))
        screen.blit(hadean_earth1, (100, 100))
        screen.blit(yrs_surface, (5, 5))
        mya_counter -= 1
        yrs_surface = YRS_FONT.render(f"{mya_counter} MYA", True, "orange")
    """
    elif room == 1:
        screen.blit(sun, (640, 360))
        screen.blit(hadean_earth1, (100, 100))
    elif room == 1:
        screen.blit(sun, (640, 360))
        screen.blit(hadean_earth1, (100, 100))
    """

    pygame.display.flip()

    clock.tick(60)

pygame.quit()