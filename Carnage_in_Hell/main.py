import pygame
from Carnage_in_Hell import menu

def start():
    pygame.init()
    WIN = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Carnage in Hell")
    menu.main_menu(WIN)  # Pass the WIN surface to main_menu function
    pygame.quit()

if __name__ == "__main__":
    start()
