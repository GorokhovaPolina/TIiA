import numpy as np

def encode_hamming(data_bits):
    """
    Кодирование данных с использованием кода Хэмминга.
    :param data_bits: Список информационных бит (k-битовое сообщение)
    :return: Закодированное сообщение с проверочными битами
    """
    # Число информационных бит
    k = len(data_bits)
    
    # Определяем число проверочных бит (r) по формуле 2^r - r - 1 >= k
    r = 0
    while (2**r - r - 1) < k:
        r += 1
    
    # Общее количество бит в закодированном сообщении
    n = 2**r - 1

    # Создаем список для хранения закодированного сообщения
    encoded_message = [0] * n

    # Заполняем информационные биты на не-кратных позициях степеням двойки
    j = 0
    for i in range(1, n + 1):
        if not (i & (i - 1)) == 0:  # Проверяем, что i не является степенью 2
            encoded_message[i - 1] = data_bits[j]
            j += 1

    # Рассчитываем проверочные биты
    for i in range(r):
        parity_position = 2**i
        parity_sum = 0
        for j in range(1, n + 1):
            if j & parity_position:  # Если бит участвует в чётности
                parity_sum ^= encoded_message[j - 1]  # XOR всех битов
        encoded_message[parity_position - 1] = parity_sum

    return encoded_message

def decode_hamming(encoded_message):
    """
    Декодирование закодированного сообщения и исправление одной ошибки (если она есть).
    :param encoded_message: Закодированное сообщение (n-битовое сообщение)
    :return: Декодированное сообщение (k-битовое) и позиция исправленной ошибки (если она есть)
    """
    n = len(encoded_message)
    
    # Определяем количество проверочных бит
    r = 0
    while (2**r - 1) < n:
        r += 1

    # Вычисляем синдром, проверяя чётность
    syndrome = 0
    for i in range(r):
        parity_position = 2**i
        parity_sum = 0
        for j in range(1, n + 1):
            if j & parity_position:  # Если бит участвует в чётности
                parity_sum ^= encoded_message[j - 1]
        if parity_sum != 0:
            syndrome += parity_position

    # Если синдром ненулевой, значит есть ошибка
    if syndrome > 0:
        print(f"Ошибка в позиции: {syndrome}")
        # Исправляем ошибку путем инверсии бита на этой позиции
        encoded_message[syndrome - 1] ^= 1
    
    # Извлекаем информационные биты (игнорируем позиции проверочных битов)
    decoded_message = []
    for i in range(1, n + 1):
        if not (i & (i - 1)) == 0:  # Не проверочные биты (не степени двойки)
            decoded_message.append(encoded_message[i - 1])

    return decoded_message, syndrome if syndrome > 0 else None

# Пример информационного сообщения
data_bits = [1, 0, 1, 1]  # Сообщение длиной k=4

# Кодируем сообщение
encoded_message = encode_hamming(data_bits)
print("Закодированное сообщение:", encoded_message)

# Вносим ошибку для тестирования (например, меняем 3-й бит)
encoded_message[2] ^= 1
print("Сообщение с ошибкой:", encoded_message)

# Декодируем и исправляем ошибку
decoded_message, error_position = decode_hamming(encoded_message)
print("Декодированное сообщение:", decoded_message)
if error_position:
    print(f"Исправлена ошибка в позиции: {error_position}")
else:
    print("Ошибок нет.")