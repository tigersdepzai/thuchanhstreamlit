import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Con chim nhảy nhảy 🐦")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Thiết lập chim
bird = pygame.Rect(50, 300, 30, 30)
bird_speed = 0
gravity = 0.5
jump_strength = -10

# Ống
pipes = []
pipe_width = 50
pipe_gap = 150
pipe_speed = 3

# Đồng hồ
clock = pygame.time.Clock()

# Font chữ
font = pygame.font.SysFont(None, 36)
score = 0

def add_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
    pipes.append((top_pipe, bottom_pipe))

# Thêm ống ban đầu
add_pipe()

# Vòng lặp trò chơi
running = True
while running:
    screen.fill(BLUE)

    # Sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = jump_strength

    # Cập nhật chim
    bird_speed += gravity
    bird.y += int(bird_speed)

    # Kiểm tra va chạm sàn/trần
    if bird.top < 0 or bird.bottom > HEIGHT:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Vẽ chim
    pygame.draw.rect(screen, WHITE, bird)

    # Cập nhật và vẽ ống
    new_pipes = []
    for top_pipe, bottom_pipe in pipes:
        top_pipe.x -= pipe_speed
        bottom_pipe.x -= pipe_speed

        if top_pipe.right > 0:
            new_pipes.append((top_pipe, bottom_pipe))
        else:
            score += 1
            add_pipe()

        # Va chạm
        if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Vẽ ống
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)

    pipes = new_pipes

    # Hiển thị điểm
    score_text = font.render(f"Điểm: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)
