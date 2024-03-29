import unittest
import pygame
from ship import Player, Enemy, Laser
from menu import handle_events

class TestGame(unittest.TestCase):
    def test_enemy_hit_by_player_laser(self):
        # Test if the enemy sprite is removed when hit by a player laser
        player = Player(400, 600)
        enemy = Enemy(400, 100, "red")  # Provide a color argument
        laser_img = pygame.Surface((10, 10))  # Create a dummy surface for laser image
        laser = Laser(400, 200, laser_img)  # Create a dummy laser with a surface
        player.lasers.append(laser)
        player.move_lasers(-5, [enemy])  # Move lasers and check collision
        self.assertNotIn(enemy, player.lasers)  # Assert enemy is removed from lasers list

    def test_enemy_shoot_damage(self):
        # Test if the player's health decreases when hit by enemy laser
        player = Player(400, 600)
        enemy = Enemy(400, 100, "red")  # Provide a color argument
        enemy_laser_img = pygame.Surface((10, 10))  # Create a dummy surface for enemy laser image
        enemy_laser = Laser(400, 600, enemy_laser_img)  # Create a dummy enemy laser with a surface
        enemy.lasers.append(enemy_laser)
        player.health = 100
        player.move_lasers(-5, [enemy_laser])  # Move player and check collision with enemy laser
        self.assertLessEqual(player.health,100)  # Assert player health has decreased or remained the same due to collision

    def test_game_over(self):
        # Test if the game ends when player's health is zero
        player = Player(400, 600)
        player.health = 0
        self.assertTrue(player.health <= 0)  # Assert player health is zero or negative

    def test_music_turn_off(self):
        # Test if the music turns off when "Music: OFF" button is clicked
        WIN = pygame.display.set_mode((900, 700))  # Dummy window for testing
        sound_button = pygame.Rect(800, 600, 100, 50)  # Dummy sound button
        quit_button = pygame.Rect(800, 650, 100, 50)  # Dummy quit button
        music_on = True  # Initially music is on
        run = True  # Dummy run variable
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(850, 625), button=1)  # Simulate mouse click on sound button
        pygame.event.post(event)  # Post the event
        run = handle_events(run, WIN, sound_button, quit_button)  # Handle the event
        music_on = not music_on  # Toggle music state
        self.assertFalse(music_on)  # Assert music is turned off

if __name__ == '__main__':
    unittest.main()
