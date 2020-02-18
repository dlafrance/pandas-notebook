import numpy as np

# 2: Create array and experiment
simple_array = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
print(simple_array)

print(f'Array dimension:', simple_array.ndim)
print(f'Array shape:', simple_array.shape)
print(f'Array size:', simple_array.size)
print(f'Array type:', simple_array.dtype)

# 3: Create matrix and experiment
matrix = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
print(matrix)

print(f'Matrix dimension:', matrix.ndim)
print(f'Matrix shape:', matrix.shape)
print(f'Matrix size:', matrix.size)
print(f'Matrix type:', matrix.dtype)

# 4: Create 1 dimension array
print(f'Range array:', np.arange(1, 10))
print(f'Random array:', np.random.rand(5))

# 5: Create 2 dimension matrix
print(f'Zeros matrix:\n', np.zeros((4, 4)))
print(f'Random matrix:\n', np.random.rand(4, 4))

# 6 Create arrays and reshape
seven_array = np.ones(20) * 7
print(seven_array)

seven_matrix = seven_array.reshape(4, 5)
print(seven_matrix)

# 7 Create 6x6 matrix
array_36 = np.arange(1, 37)
matrix_36 = array_36.reshape(6, 6)
print(f' Reshaped to matrix: \n', matrix_36)

print(f' First element:', matrix_36[0, 0])
print(f' Last 2 rows:\n', matrix_36[-2:, :])
print(f' Mid 2:\n', matrix_36[2:4, 2:4])
print(f' Sum of column values:\n', matrix_36.sum(axis=0))
