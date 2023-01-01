import pygame
from food import Food

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "UP"
        self.body = [(x, y), (x, y+1), (x, y+2)]

    def update(self, food):
        # Update the snake's position based on its direction
        if self.direction == "UP":
            self.y += 1
        elif self.direction == "DOWN":
            self.y -= 1
        elif self.direction == "LEFT":
            self.x -= 1
        elif self.direction == "RIGHT":
            self.x += 1

        self.body.insert(0, (self.x, self.y))
        # Update the snake's body segments
        if (food.x, food.y) not in self.body:
            self.body.pop()


    def draw(self, screen):
        # Draw the snake to the screen
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0]*20, segment[1]*20, 20, 20))
