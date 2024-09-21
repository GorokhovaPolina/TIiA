import numpy as np

def repetition_g_to_h(g_matrix, r):
    """
    Получение контрольной матрицы H для кода с повторением из генераторной матрицы G.
    :param g_matrix: Генераторная матрица G (k x n)
    :param r: Число повторений для каждого бита (r)
    :return: Контрольная матрица H (n - k x n)
    """
    g = np.array(g_matrix)
    k, n = g.shape
    
    # Контрольная матрица для кода с повторением будет размером (n - k) x n
    h = np.zeros((n - k, n), dtype=int)
    
    # Заполняем H так, чтобы каждая группа повторяющихся бит проверялась
    row = 0
    for i in range(k):
        for j in range(r - 1):
            h[row, i * r + j] = 1
            h[row, i * r + j + 1] = 1
            row += 1

    return h.tolist()

def repetition_h_to_g(h_matrix, r):
    """
    Получение генераторной матрицы G для кода с повторением из контрольной матрицы H.
    :param h_matrix: Контрольная матрица H (n - k x n)
    :param r: Число повторений для каждого бита (r)
    :return: Генераторная матрица G (k x n)
    """
    h = np.array(h_matrix)
    _, n = h.shape
    
    # Число информационных бит
    k = n // r
    
    # Генераторная матрица будет размером k x n
    g = np.zeros((k, n), dtype=int)
    
    # Заполняем G, каждая строка содержит r подряд идущих единиц
    for i in range(k):
        g[i, i * r:(i + 1) * r] = 1

    return g.tolist()

# Пример генераторной матрицы для кода с повторением (r = 3)
g_matrix = [
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
]

# Получаем контрольную матрицу H из G для кода с повторением (r = 3)
h_matrix_from_g = repetition_g_to_h(g_matrix, r=3)
print("Контрольная матрица H из G:")
print(np.array(h_matrix_from_g))

# Получаем генераторную матрицу G из H для кода с повторением (r = 3)
g_matrix_from_h = repetition_h_to_g(h_matrix_from_g, r=3)
print("Генераторная матрица G из H:")
print(np.array(g_matrix_from_h))