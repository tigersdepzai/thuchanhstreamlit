
import pygame, sys, random
pygame.init()
score = 0
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
PLAYER_SPEED = 5
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
    global score
    for i in range(len(enemy_list)):
        if enemy_list[i][1] < SCREEN_HEIGHT:
            enemy_list[i][1] += ENEMY_SPEED
        else:
            score += 1
            enemy_list[i][1] = random.randint(-SCREEN_HEIGHT, 0)
            enemy_list[i][0] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and PLAYER_POS[0] > 0:
        PLAYER_POS[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and PLAYER_POS[0] < SCREEN_WIDTH - PLAYER_SIZE:
        PLAYER_POS[0] += PLAYER_SPEED

def detect_collision(obj1_pos, obj2_pos):
    obj1_x, obj1_y = obj1_pos
    obj2_x, obj2_y = obj2_pos

    if (obj1_x < obj2_x + ENEMY_SIZE and
        obj1_x + PLAYER_SIZE > obj2_x and
        obj1_y < obj2_y + ENEMY_SIZE and
        obj1_y + PLAYER_SIZE > obj2_y):
        return True
    return False

def check_collisions():
    for enemy_pos in enemy_list:
        if detect_collision(PLAYER_POS, enemy_pos):
            return True
    return False

game_over = False
while not game_over:
    game_over = handle_events()
    update_enemy()

    if check_collisions():
        game_over = True
    draw_objects()
    font = pygame.font.SysFont("monospace", 36)
    text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(text, (10, 10))
    pygame.display.update()