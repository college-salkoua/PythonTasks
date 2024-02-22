from src.open_tasks import open_it
import os


def first_task():
    def fibonacci_recursive(k, n):
        if k <= 1:
            return k
        else:
            return fibonacci_recursive(k - 1, n) + fibonacci_recursive(k - 2, n)

    k = int(input("Введіть початковий індекс (k): "))
    n = int(input("Введіть кінцевий індекс (n): "))

    print("Числа Фібоначчі від {}-го до {}-го:".format(k, n))
    for i in range(k, n + 1):
        print(fibonacci_recursive(i, n))


def second_task():
    def fibonacci_special(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 3
        elif n == 3:
            return 4
        else:
            return fibonacci_special(n - 1) + fibonacci_special(n - 2)

    def print_special_fibonacci_sequence(n):
        for i in range(1, n + 1):
            print(fibonacci_special(i), end=" ")

    n = int(input("Введіть кількість чисел Фібоначчі, які треба згенерувати: "))
    print("Перші", n, "чисел Фібоначчі зі спеціальним виглядом:")
    print_special_fibonacci_sequence(n)


def third_task():
    def is_valid_move(matrix, visited, row, col):
        # Перевірка на виходження за межі матриці та чи комірка не відвідана і має значення 1
        return (
            row >= 0
            and row < len(matrix)
            and col >= 0
            and col < len(matrix[0])
            and not visited[row][col]
            and matrix[row][col] == 1
        )

    def DFS(matrix, visited, row, col):
        # Відносно всіх можливих ходів
        # Верх, Низ, Ліво, Право, Діагональ по горизонталі, Діагональ по вертикалі
        row_moves = [-1, 1, 0, 0, -1, 1, -1, 1]
        col_moves = [0, 0, -1, 1, -1, -1, 1, 1]

        # Відмітка комірки як відвіданої
        visited[row][col] = True

        # Перевірка сусідніх комірок
        for i in range(8):
            if is_valid_move(matrix, visited, row + row_moves[i], col + col_moves[i]):
                DFS(matrix, visited, row + row_moves[i], col + col_moves[i])

    def count_islands(matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited[i][j]:
                    DFS(matrix, visited, i, j)
                    count += 1

        return count

    # Приклад використання
    matrix = [[1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 1, 1], [1, 0, 1, 0]]

    print("Кількість фігур, що утворюють одиниці:", count_islands(matrix))


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
