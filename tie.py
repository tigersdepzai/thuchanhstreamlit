def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Kiểm tra hàng, cột, đường chéo
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Lượt của người chơi {current_player}")
        try:
            row = int(input("Nhập hàng (0, 1, 2): "))
            col = int(input("Nhập cột (0, 1, 2): "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
            continue

        if row not in range(3) or col not in range(3):
            print("Vị trí không hợp lệ. Thử lại!")
            continue
        if board[row][col] != " ":
            print("Ô này đã được đánh rồi. Chọn ô khác!")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Người chơi {current_player} chiến thắng!")
            break
        if is_draw(board):
            print_board(board)
            print("Trò chơi hòa!")
            break

        # Đổi người chơi
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
