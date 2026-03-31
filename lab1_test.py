import numpy as np
import unittest
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def add_matrices_byte(a, b):
    a_np = np.array(a, dtype=np.int8)
    b_np = np.array(b, dtype=np.int8)
    if a_np.shape != b_np.shape:
        raise ValueError("Matrices must have the same dimensions")
    return a_np + b_np

def calculate_sum_of_mins(matrix):
    return np.sum(np.min(matrix, axis=0))

class TestMatrixOperations(unittest.TestCase):
    def test_byte_overflow(self):
        self.assertEqual(add_matrices_byte([[127]], [[1]])[0][0], -128)

    def test_sum_of_mins(self):
        matrix = np.array([[10, 5], [20, 2]])
        self.assertEqual(calculate_sum_of_mins(matrix), 12)

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            add_matrices_byte([[1, 2]], [[1, 2, 3]])

def read_unicode_test_file(lab1_proga):
    try:
        with open(lab1_proga, 'r', encoding='utf-8') as f:
            print(f.read())
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixOperations)
    unittest.TextTestRunner(verbosity=2).run(suite)

    A = [[10, 20, 30], [40, 50, 60]]
    B = [[1, 2, 3], [4, 5, 6]]

    try:
        C = add_matrices_byte(A, B)
        print("\nMatrix C:")
        print(C)
        print(f"Sum of mins: {calculate_sum_of_mins(C)}")
    except Exception as e:
        print(e)

    print("\nFile content:")
    read_unicode_test_file('unicode_test.txt')