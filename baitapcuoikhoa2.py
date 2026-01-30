import pygame
import random
import sys

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("hứng trái cây rơi")


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)


player_width = 60
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 7


fruit_size = 35
fruit_speed = 2
number_of_fruits = 4
fruit_list = []

for i in range(number_of_fruits):
    fruit_x = random.randint(0, screen_width - fruit_size)
    fruit_y = random.randint(-screen_height, 0)
    fruit_list.append([fruit_x, fruit_y])


score = 0
lives = 3
clock = pygame.time.Clock()


def draw_game_screen():
    screen.fill(COLOR_BLACK)
    pygame.draw.rect(screen, COLOR_WHITE, (player_x, player_y, player_width, player_height))
    for fruit in fruit_list:
        pygame.draw.rect(screen, COLOR_RED, (fruit[0], fruit[1], fruit_size, fruit_size))


    for fruit in fruit_list:
        fruit[1] += fruit_speed

        
        if fruit[1] > screen_height:
            lives -= 1
            fruit[0] = random.randint(0, screen_width - fruit_size)
            fruit[1] = random.randint(screen_height, 0)


def check_collision(player_x, player_y, fruit_x, fruit_y):
    if (player_x < fruit_x + fruit_size and
        player_x + player_width > fruit_x and
        player_y < fruit_y + fruit_size and
        player_y + player_height > fruit_y):
        return True
    else:
        return False
def handle_player_hit():
    global score

    for fruit in fruit_list:
        fruit_x = fruit[0]
        fruit_y = fruit[1]

        if check_collision(player_x, player_y, fruit_x, fruit_y):
            score += 1
            fruit[0] = random.randint(0, screen_width - fruit_size)
            fruit[1] = random.randint(-screen_height, 0)

while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    move_fruits()
    handle_player_hit()

    if lives <= 0:
        game_running = False

    draw_game_screen()

    font = pygame.font.Font(None, 34)
    display_text = font.render("Score: " + str(score) + "    Lives: " + str(lives), True, COLOR_GREEN)
    screen.blit(display_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
