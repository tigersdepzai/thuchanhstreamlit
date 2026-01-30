import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


dino_x = 50
dino_y = 300
dino_width = 40
dino_height = 40
dino_vel = 0
gravity = 0.5
jump_strength = -10


obstacles = []
obstacle_width = 20
obstacle_height = 40
obstacle_speed = 5
spawn_time = 1500  # mili giây

# Đồng hồ
clock = pygame.time.Clock()


pygame.time.set_timer(pygame.USEREVENT + 1, spawn_time)

def draw_window():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (dino_x, int(dino_y), dino_width, dino_height))
    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, obs)
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_y + dino_height >= HEIGHT:
                dino_vel = jump_strength
        if event.type == pygame.USEREVENT + 1:
            obs_x = WIDTH
            obs_y = HEIGHT - obstacle_height
            obstacles.append(pygame.Rect(obs_x, obs_y, obstacle_width, obstacle_height))

    # Cập nhật vị trí khủng long
    dino_vel += gravity
    dino_y += dino_vel
    if dino_y + dino_height > HEIGHT:
        dino_y = HEIGHT - dino_height
        dino_vel = 0

    # Cập nhật vị trí obstacle
    for obs in obstacles:
        obs.x -= obstacle_speed
    obstacles = [obs for obs in obstacles if obs.x + obstacle_width > 0]

    # Kiểm tra va chạm
    dino_rect = pygame.Rect(dino_x, int(dino_y), dino_width, dino_height)
    for obs in obstacles:
        if dino_rect.colliderect(obs):
            print("Game Over!")
            run = False

    draw_window()

pygame.quit()
sys.exit()



