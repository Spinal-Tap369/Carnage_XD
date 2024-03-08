# menu.py

import pygame
import game
import sys

def main_menu(WIN):
    run = True
    clock = pygame.time.Clock()

    start_button = pygame.Rect(WIN.get_width() // 2 - 100, 300, 200, 50)
    quit_button = pygame.Rect(WIN.get_width() // 2 - 100, 400, 200, 50)

    while run:
        WIN.fill((0, 0, 0))
        draw_menu(WIN, start_button, quit_button)
        run = handle_events(run, WIN, start_button, quit_button)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def draw_menu(WIN, start_button, quit_button):
    title_font = pygame.font.SysFont("comicsans", 70)
    button_font = pygame.font.SysFont("comicsans", 40)
    instruction_font = pygame.font.SysFont("comicsans", 30)

    title_label = title_font.render("Carnage in Hell", 1, (255, 255, 255))
    WIN.blit(title_label, (WIN.get_width() // 2 - title_label.get_width() // 2, 100))

    pygame.draw.rect(WIN, (128, 128, 128), start_button)
    pygame.draw.rect(WIN, (128, 128, 128), quit_button)

    start_label = button_font.render("Start Game", 1, (255, 255, 255))
    WIN.blit(start_label, (
        start_button.centerx - start_label.get_width() // 2, start_button.centery - start_label.get_height() // 2))

    quit_label = button_font.render("Quit Game", 1, (255, 255, 255))
    WIN.blit(quit_label, (
        quit_button.centerx - quit_label.get_width() // 2, quit_button.centery - quit_label.get_height() // 2))

    instruction_text = "Hit, don't get hit, and don't let them cross."
    instruction_label = instruction_font.render(instruction_text, 1, (255, 255, 255))
    WIN.blit(instruction_label, (WIN.get_width() // 2 - instruction_label.get_width() // 2, 500))

def handle_events(run, WIN, start_button, quit_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game.main(WIN)
                return True
            elif quit_button.collidepoint(event.pos):
                return False

    return run
