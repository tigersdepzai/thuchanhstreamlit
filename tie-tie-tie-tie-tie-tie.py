import pygame, sys

pygame.init()

SREEN_WIDTH = 600
SCREEN_HEIGHT = 600
pygame.display.set_caption("TIE TIE TIE TIE TIE TIE")
screen = pygame.display.set_mode((SREEN_WIDTH, SCREEN_HEIGHT))

ROWS = 3
COLS = 3
SQUARE_SIZE = SREEN_WIDTH // COLS
LINE_WIDTH = 10
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen.fill(BG_COLOR)
board = [[0 for i in range(COLS)] for j in range(ROWS)]

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (SREEN_WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SREEN_WIDTH), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SREEN_WIDTH), LINE_WIDTH)

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                  row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

def check_win(player):
    # Horizontal
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_row(row, player)
            return True

    # Vertical
    for col in range(COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_col(col, player)
            return True

    # Desc diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    # Asc diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    return False

def draw_vertical_col(col, player):
    pygame.draw.line(screen, RED,
                     (col * SQUARE_SIZE + SQUARE_SIZE // 2, 15),
                     (col * SQUARE_SIZE + SQUARE_SIZE // 2, SREEN_WIDTH - 15),
                     15)

def draw_horizontal_row(row, player):
    pygame.draw.line(screen, RED,
                     (15, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                     (SREEN_WIDTH - 15, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                     15)

def draw_desc_diagonal(player):
    pygame.draw.line(screen, RED, (15, 15), (SREEN_WIDTH - 15, SREEN_WIDTH - 15), 15)

def draw_asc_diagonal(player):
    pygame.draw.line(screen, RED, (15, SREEN_WIDTH - 15), (SREEN_WIDTH - 15, 15), 15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

draw_lines()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = 2 if player == 1 else 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
