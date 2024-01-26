import pygame
import sys
from language_menu import language_call
from help_menu import help_call

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Menu():
    def initialize(self):
        pygame.init()

        # Set up the screen
        screen_width = 1000
        screen_height = 1000
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Omilia")

        # Load images
        bg_img = pygame.image.load("menuAssets/oi.png")
        start_button_img = pygame.image.load("menuAssets/start1.png")
        help_button_img = pygame.image.load("menuAssets/help1.png")
        pygame.mixer.music.load("menuAssets/menubg.wav")
        pygame.mixer.music.play(-1)
        # Create Rect objects for the buttons
        start_button_rect = pygame.Rect(
            380, 430, start_button_img.get_width(), start_button_img.get_height()
        )
        help_button_rect = pygame.Rect(
            380, 550, help_button_img.get_width(), help_button_img.get_height()
        )

        # Main loop
        while True:
            # Draw the background and buttons
            screen.blit(bg_img, (0, 0))
            screen.blit(start_button_img, start_button_rect)
            screen.blit(help_button_img, help_button_rect)
            while Gtk.events_pending():
                Gtk.main_iteration()
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse clicked on a button
                    if start_button_rect.collidepoint(event.pos):
                        language_call()
                    elif help_button_rect.collidepoint(event.pos):
                        help_call()

            # Update the screen
            pygame.display.update()
            
    def run(self):
        self.initialize()


if __name__ == "__main__":
    menu = Menu()
    menu.run()