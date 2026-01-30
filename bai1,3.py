# câu 1     # Vẽ hình chữ nhật màu đỏ
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((500, 500))
RED = (255, 0, 0)
WHITE = (255, 255, 255)
screen.fill(WHITE)

pygame.draw.rect(screen, RED, (100, 100, 300, 300))
pygame.display.update()
# câu 2    # Vẽ hình tròn màu xanh
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 150)
pygame.display.update()
# câu 3    # Vẽ một đường thẳng màu trắng
pygame.draw.line(screen, (255, 255, 255), (0, 0), (500, 500), 5)
pygame.display.update()
# câu 4    # Vẽ nhiều hình khác nhau
pygame.draw.polygon(screen, (0, 255, 0), [(100, 400), (200, 300), (300, 400)])
pygame.draw.ellipse(screen, (255, 0, 255), (200, 200, 100, 50))
pygame.draw.arc(screen, (0, 255, 255), (50, 50, 400, 400), 0, 3.14, 5)
pygame.display.update()
#câu 5    # Vẽ một ngôi nhà
pygame.draw.rect(screen, (139, 69, 19), (150, 300, 200, 200))  # Mái nhà
pygame.draw.polygon(screen, (255, 0, 0), [(150, 300), (250, 200), (350, 300)])  # Mái nhà
pygame.draw.rect(screen, (255, 255, 0), (200, 350, 100, 150))  # Cửa
pygame.draw.rect(screen, (0, 0, 255), (220, 400, 60, 100))  # Cửa sổ
pygame.display.update()