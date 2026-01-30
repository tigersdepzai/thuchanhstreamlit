import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cấu hình cửa sổ game
WIDTH, HEIGHT = 500, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Đua Xe Đơn Giản 🚗")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (200, 0, 0)

# Kích thước xe
CAR_WIDTH, CAR_HEIGHT = 50, 100

# Tạo người chơi
player_car = pygame.Rect(WIDTH//2 - CAR_WIDTH//2, HEIGHT - CAR_HEIGHT - 20, CAR_WIDTH, CAR_HEIGHT)

# Tốc độ di chuyển
player_speed = 5
obstacle_speed = 5

# Kẻ thù (chướng ngại vật)
obstacles = []
spawn_delay = 30
frame_count = 0

# Font chữ
font = pygame.font.SysFont(None, 40)

# Hàm vẽ
def draw_window():
    win.fill(GRAY)

    # Đường kẻ giữa đường
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, 20))

    # Vẽ xe người chơi
    pygame.draw.rect(win, RED, player_car)

    # Vẽ chướng ngại vật
    for obs in obstacles:
        pygame.draw.rect(win, BLACK, obs)

    pygame.display.update()

# Va chạm
def check_collision():
    for obs in obstacles:
        if player_car.colliderect(obs):
            return True
    return False

# Game loop
def main():
    global frame_count
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # 60 FPS
        frame_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Điều khiển xe bằng phím trái/phải
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_car.left > 0:
            player_car.x -= player_speed
        if keys[pygame.K_RIGHT] and player_car.right < WIDTH:
            player_car.x += player_speed

        # Sinh chướng ngại vật
        if frame_count % spawn_delay == 0:
            obs_x = random.randint(0, WIDTH - CAR_WIDTH)
            new_obs = pygame.Rect(obs_x, -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
            obstacles.append(new_obs)

        # Cập nhật vị trí chướng ngại vật
        for obs in obstacles:
            obs.y += obstacle_speed

        # Xóa chướng ngại vật ngoài màn hình
        obstacles[:] = [obs for obs in obstacles if obs.y < HEIGHT]

        # Kiểm tra va chạm
        if check_collision():
            game_over_text = font.render("💥 Game Over 💥", True, RED)
            win.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
