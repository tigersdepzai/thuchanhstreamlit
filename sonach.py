import pygame, sys, random

pygame.init()

# Kích thước màn hình
screen_width = 600
screen_height = 400
title = "Con Rắn Đi Ẻ"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
AQUA = (50, 153, 213)

snake_block = 10
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25)

def show_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = font.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [10, 10])

def message(msg, color):
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(mesg, text_rect)

def game_loop():
    x_head = screen_width // 2
    y_head = screen_height // 2
    x_head_change = 0
    y_head_change = 0
    snake_list = []
    snake_length = 1

    randFoodX = random.randrange(0, screen_width - snake_block, 10)
    randFoodY = random.randrange(0, screen_height - snake_block, 10)
    foodX, foodY = randFoodX, randFoodY

    game_over = False
    speed = 12   # tốc độ ban đầu

    while True:
        while game_over:
            screen.fill(AQUA)
            message("Game Over! Space = play again | Q = out", RED)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        return game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_head_change == 0:
                    x_head_change = -10
                    y_head_change = 0
                elif event.key == pygame.K_RIGHT and x_head_change == 0:
                    x_head_change = 10
                    y_head_change = 0
                elif event.key == pygame.K_UP and y_head_change == 0:
                    x_head_change = 0
                    y_head_change = -10
                elif event.key == pygame.K_DOWN and y_head_change == 0:
                    x_head_change = 0
                    y_head_change = 10

        x_head += x_head_change
        y_head += y_head_change

        screen.fill(AQUA)
        pygame.draw.rect(screen, RED, [foodX, foodY, snake_block, snake_block])

        snake_head = [x_head, y_head]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Thua khi đâm tường
        if x_head >= screen_width or x_head < 0 or y_head >= screen_height or y_head < 0:
            game_over = True

        # Thua khi cắn trúng thân
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        # Ăn thức ăn
        if x_head == foodX and y_head == foodY:
            snake_length += 1
            randFoodX = random.randrange(0, screen_width - snake_block, 10)
            randFoodY = random.randrange(0, screen_height - snake_block, 10)
            foodX, foodY = randFoodX, randFoodY
            speed += 1   # tăng tốc độ mỗi khi ăn

        show_snake(snake_block, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()
        clock.tick(speed)

game_loop()
