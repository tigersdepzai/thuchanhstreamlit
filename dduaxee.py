
import pygame, sys, random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("game xe rơi từ trên trời xuống")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

PLAYER_SIZE = 50
ENEMY_SIZE = 30
PLAYER_POS = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE]
PLAYER_SPEED = 0.5
ENEMY_COUNT = 5
ENEMY_SPEED = 0.1

enemy_list = []
for i in range(ENEMY_COUNT):
    enemy_pos = [random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), random.randint(-SCREEN_HEIGHT, 0)]
    enemy_list.append(enemy_pos)

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))

def update_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] < SCREEN_HEIGHT:
            enemy_list[i][1] += ENEMY_SPEED
        else:
            enemy_list[i][1] = random.randint(-SCREEN_HEIGHT, 0)
            enemy_list[i][0] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and PLAYER_POS[0] > 0:
        PLAYER_POS[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and PLAYER_POS[0] < SCREEN_WIDTH - PLAYER_SIZE:
        PLAYER_POS[0] += PLAYER_SPEED
    return False

def detect_collision(odj1_pos, obj2_pos):
    obj1_x = odj1_pos[0]
    obj1_y = odj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]

    if (obj1_x <=obj2_x and obj1_x + PLAYER_SIZE >= obj2_x) or (obj2_x <= obj1_x and obj2_x + ENEMY_SIZE >= obj1_x):
        if (obj1_y <= obj2_y and obj1_y + PLAYER_SIZE >= obj2_y) or (obj2_y <= obj1_y and obj2_y + ENEMY_SIZE >= obj1_y):
            return True
    return False

def check_collisions():
    for enemy_pos in enemy_list:
        if detect_collision(PLAYER_POS, enemy_pos):
            return True
    return False

while True:
    if handle_events():
        break



    update_enemy()
    draw_objects()
    pygame.display.update()
