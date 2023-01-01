import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height):
        self.x = random.randint(0, screen_width // 20 - 1)
        self.y = random.randint(0, screen_height // 20 - 1)
        self.eaten = False

    def update(self, snake):
        # Check if the food has been eaten
        if (self.x, self.y) in snake.body:
            self.eaten = True

    def draw(self, screen):
        # Draw the food to the screen if it has not been eaten
        if not self.eaten:
            pygame.draw.rect(screen, (255, 0, 0), (self.x*20, self.y*20, 20, 20))
