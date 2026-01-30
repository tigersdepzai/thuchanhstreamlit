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
PLAYER_SPEED = 10
ENEMY_COUNT = 5
ENEMY_SPEED = 5

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    update_enemy()
    draw_objects()
    pygame.display.update()
