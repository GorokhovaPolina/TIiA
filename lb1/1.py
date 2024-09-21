# Класс, который проверяет и исправляет ошибки в линейных кодах с повторениями
class LinearCodeChecker:
    def __init__(self, generator_matrix):
        self.generator_matrix = generator_matrix

    def encode(self, message):
        """Кодирование сообщения с использованием генераторной матрицы."""
        return [sum(x * y for x, y in zip(message, row)) % 2 for row in self.generator_matrix]

    def check_codeword(self, codeword):
        """Проверка корректности закодированного слова."""
        # Проверка с использованием контрольной матрицы (пока просто для примера)
        parity_check_matrix = self._generate_parity_check_matrix()
        return all(sum(x * y for x, y in zip(codeword, row)) % 2 == 0 for row in parity_check_matrix)

    def correct_codeword(self, codeword):
        """Исправление ошибок в закодированном слове, если это возможно."""
        if self.check_codeword(codeword):
            return codeword  # Кодовое слово корректно

        # Попробуем исправить одну ошибку (для простоты)
        for i in range(len(codeword)):
            # Создаем новое кодовое слово, инвертируя i-тый бит
            candidate = codeword[:]
            candidate[i] ^= 1  # Инвертируем бит

            if self.check_codeword(candidate):
                return candidate  # Возвращаем исправленное слово

        raise ValueError("Не удалось исправить кодовое слово.")

    def _generate_parity_check_matrix(self):
        """Генерация контрольной матрицы (для примера, будет случайной)."""
        import random
        rows = len(self.generator_matrix[0]) - len(self.generator_matrix)
        cols = len(self.generator_matrix[0])
        return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Пример использования:
generator_matrix = [
    [1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1],
]

checker = LinearCodeChecker(generator_matrix)

# Кодируем сообщение
message = [1, 0, 1]
codeword = checker.encode(message)
print("Закодированное слово:", codeword)

# Проверяем кодовое слово
is_correct = checker.check_codeword(codeword)
print("Кодовое слово корректно:", is_correct)

# Исправляем кодовое слово
corrupted_codeword = codeword[:]
corrupted_codeword[1] ^= 1  # Создаем ошибку
print("Испорченное кодовое слово:", corrupted_codeword)

corrected_codeword = checker.correct_codeword(corrupted_codeword)
print("Исправленное кодовое слово:", corrected_codeword)