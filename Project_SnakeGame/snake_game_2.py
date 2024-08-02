### Course: Zero ta Mestery Academy | Prompt Engineering
### Project: Building a Snake Game
### project_snakeGame2.py: Snake Game Version 2 (fully functional and customized)

### imports
import pygame
import random

### initializing pygame
pygame.init()

### display setup
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

### color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (128, 0, 128)
steelblue = (70, 130, 180)
orange = (255, 165, 0)

### game parameters
snake_block = 10
snake_speed = 10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 28)
score_font = pygame.font.SysFont(None, 25)

### function rendering game score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    window.blit(value, [0, 0])

### function drawing the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, steelblue, [x[0], x[1], snake_block, snake_block])

### function rendering end of game message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(width/2,height/2))
    window.blit(mesg, mesg_rect)

### game loop function
def gameLoop():

    ### game termination flags
    game_over = False
    game_close = False

    ### snake parameter inits
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1

    ### initial food coordinates
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    ### executing game
    while not game_over:

        ### terminating game
        while game_close:
            window.fill(white)
            message("Game Over! Womp Womp. Press Q to quit or C to play again.", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        ### collecting user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, orange, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()

