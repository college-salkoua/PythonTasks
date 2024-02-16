from src.open_tasks import open_it
import os


def first_task():
    def create_board():
        board = [[" " for _ in range(3)] for _ in range(3)]
        return board

    def display_board(board):
        for row in board:
            print("|".join(row))
            print("-" * 5)

    def check_winner(board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(
                board[j][i] == player for j in range(3)
            ):
                return True
        if all(board[i][i] == player for i in range(3)) or all(
            board[i][2 - i] == player for i in range(3)
        ):
            return True
        return False

    def tic_tac_toe():
        board = create_board()
        current_player = "X"
        game_over = False

        while not game_over:
            display_board(board)
            print(f"Гравець {current_player}, ваш хід.")

            row = int(input("Введіть номер рядка (1-3): ")) - 1
            col = int(input("Введіть номер стовпця (1-3): ")) - 1

            if board[row][col] == " ":
                board[row][col] = current_player

                if check_winner(board, current_player):
                    display_board(board)
                    print(f"Гравець {current_player} переміг!")
                    game_over = True

                elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                    display_board(board)
                    print("Нічия!")
                    game_over = True

                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Ця клітинка вже зайнята. Спробуйте ще раз.")

    tic_tac_toe()


def second_task():
    def count_holes(n):

        if isinstance(n, int) or (isinstance(n, str) and n.isdigit()):

            if isinstance(n, str):
                n = int(n)

            hole_count = 0
            for digit in str(n):
                if digit == "4":
                    hole_count += 1
                elif digit == "0":
                    hole_count += 1
            return hole_count
        else:
            return "ERROR"

    print(count_holes(123))

    print(count_holes(404))

    print(count_holes("456789"))

    print(count_holes("840"))

    print(count_holes("abc"))


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
