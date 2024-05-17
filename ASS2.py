import numpy as np

# Dot Method

# Example 1
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result_1 = np.dot(A, B)
print("Dot product (Example 1):")
print(result_1)

# Example 2
C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[7, 8], [9, 10], [11, 12]])
result_2 = np.dot(C, D)
print("\nDot product (Example 2):")
print(result_2)

# Example 3
E = np.array([[2, 3], [4, 5], [6, 7]])
F = np.array([1, 2])
result_3 = np.dot(E, F)
print("\nDot product (Example 3):")
print(result_3)

# Transpose Method

# Example 1
M = np.array([[1, 2], [3, 4], [5, 6]])
transposed_1 = np.transpose(M)
print("\nTransposed matrix (Example 1):")
print(transposed_1)

# Example 2
N = np.array([[1, 2, 3], [4, 5, 6]])
transposed_2 = np.transpose(N)
print("\nTransposed matrix (Example 2):")
print(transposed_2)

# Example 3
O = np.array([[1], [2], [3]])
transposed_3 = np.transpose(O)
print("\nTransposed matrix (Example 3):")
print(transposed_3)

# linalg.inv Method

# Example 1
P = np.array([[1, 2], [3, 4]])
inverse_1 = np.linalg.inv(P)
print("\nInverse matrix (Example 1):")
print(inverse_1)

# Example 2
Q = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
inverse_2 = np.linalg.inv(Q)
print("\nInverse matrix (Example 2):")
print(inverse_2)

# Example 3
R = np.array([[4, 7], [2, 6]])
inverse_3 = np.linalg.inv(R)
print("\nInverse matrix (Example 3):")
print(inverse_3)

# linalg.det Method

# Example 1
S = np.array([[1, 2], [3, 4]])
determinant_1 = np.linalg.det(S)
print("\nDeterminant (Example 1):", determinant_1)

# Example 2
T = np.array([[3, 2], [6, 4]])
determinant_2 = np.linalg.det(T)
print("\nDeterminant (Example 2):", determinant_2)

# Example 3
U = np.array([[2, 5, 3], [1, -2, -1], [1, 3, 4]])
determinant_3 = np.linalg.det(U)
print("\nDeterminant (Example 3):", determinant_3)

# Flatten Method

# Example 1
V = np.array([[1, 2, 3], [4, 5, 6]])
flattened_1 = V.flatten()
print("\nFlattened array (Example 1):", flattened_1)

# Example 2
W = np.array([[1, 2], [3, 4]])
flattened_2 = W.flatten()
print("\nFlattened array (Example 2):", flattened_2)

# Example 3
X = np.array([[1, 2, 3]])
flattened_3 = X.flatten()
print("\nFlattened array (Example 3):", flattened_3)
