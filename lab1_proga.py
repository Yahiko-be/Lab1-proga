#Дія: C = A + B
#Тип елементів: byte
#Дія з матрицею C: Обчислити суму найменших елементів кожного стовпця

import numpy as np


def solve_matrix_task():
    try:
        matrix_a = np.array([
            [10, 20, 30],
            [40, 50, 60]
        ], dtype=np.int8)

        matrix_b = np.array([
            [1, 2, 3],
            [4, 5, 6]
        ], dtype=np.int8)

        matrix_c = matrix_a + matrix_b

        print("Матриця C (A + B):")
        print(matrix_c)

        min_in_columns = np.min(matrix_c, axis=0)

        total_sum_of_mins = np.sum(min_in_columns)

        print(f"\nМінімальні елементи в кожному стовпці: {min_in_columns}")
        print(f"Сума найменших елементів: {total_sum_of_mins}")

    except ValueError as e:
        print(f"Помилка розмірності: {e}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")


if __name__ == "__main__":
    solve_matrix_task()