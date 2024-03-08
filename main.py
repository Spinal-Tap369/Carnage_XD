#main.py

import pygame
import menu

if __name__ == "__main__":
    pygame.init()
    WIN = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Space Shooter Tutorial")
    menu.main_menu(WIN)  # Pass the WIN surface to main_menu function
    pygame.quit()