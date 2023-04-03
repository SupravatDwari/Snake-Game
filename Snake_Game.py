import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("Snake Game")

# Set clock for refreshing screen
clock = pygame.time.Clock()

# Set font for displaying score
font = pygame.font.SysFont(None, 30)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Define block size for snake and food
block_size = 10

# Define function for displaying score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [0, 0])

# Define function for drawing snake
def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])

# Define function for displaying message on screen
def message(msg,color):
    text = font.render(msg,True,color)
    screen.blit(text,[screen_width/6,screen_height/3])

# Define main game loop
def gameLoop():
    # Set initial position of snake
    x1 = screen_width/2
    y1 = screen_height/2
    x1_change = 0
    y1_change = 0

    # Set initial length of snake
    snake_list = []
    snake_length = 1

    # Set initial position of food
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Set initial score
    score = 0

    # Set flag for game over
    game_over = False

    # Start game loop
    while not game_over:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Update position of snake
        x1 += x1_change
        y1 += y1_change

        # Check if snake hits the boundary of the screen
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        # Draw background color
        screen.fill(black)

        # Draw food on screen
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        # Update snake length and score if it eats food
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            snake_length += 1
            score += 1
        # Check if snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # Draw snake on screen
        draw_snake(snake_list)

        # Display score
        display_score(score)

        # Refresh screen
        pygame.display.update()

        # Set refresh rate
        clock.tick(20)

    # Game over message
    message("Game Over!", red)
    pygame.display.update()
    clock.tick(2)

    # Quit game
    pygame.quit()
    quit()

# Call main game loop
gameLoop()
