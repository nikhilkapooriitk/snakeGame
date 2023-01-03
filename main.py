import sys
import pygame
from snake import Snake
from food import Food
from score import Score


def restartGame(snake, food, score):
    snake = Snake(0,0)
    food = Food(640,480)
    score.resetScore()


# Initialize Pygame
pygame.init()

# Set the window size and create a display surface
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create an instance of the Snake object
snake = Snake(0, 0)

# Create an instance of the Food object
food = Food(640, 480)

#Create an instance of Score object
score = Score()

# Main game loop
while True:
    # Handle input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.direction = "UP"
            elif event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            elif event.key == pygame.K_UP:
                snake.direction = "DOWN"
            elif event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"

    # Update the snake's position and check for collisions
    snake.update(food)

    # Check for a collision between the snake and the wall
    if snake.x < 0 or snake.x > 640 // 20 - 1 or snake.y < 0 or snake.y > 480 // 20 - 1:
        # Restart the game
        #restartGame(snake= snake, food= food, score= score)
        snake = Snake(0, 0)
        food = Food(640, 480)
        
    #check if snake has bitten itself
    if (snake.x, snake.y) in snake.body[1:]:
        #Restart the game
        snake = Snake(0, 0)
        food = Food(640, 480)

    # Update the food's position if it has been eaten
    food.update(snake)
    if food.eaten:
        food = Food(640, 480)
        score.updateScore()
        

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake and food to the screen
    snake.draw(screen)
    food.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(7)


