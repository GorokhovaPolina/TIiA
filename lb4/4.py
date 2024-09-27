
from collections import Counter
import math

def Fano_coding(syms):  # кодирование с помощью условия Фано
    if len(syms) == 1:
        return {syms[0][0]: '0'}
    
    syms = sorted(syms, key=lambda x: x[1], reverse=True)
    total = sum([symbol[1] for symbol in syms]) 
    
    # Разделение списка по условию Фано
    acc = 0
    split_index = 0
    for i, symbol in enumerate(syms):
        acc += symbol[1]
        if acc >= total / 2:
            split_index = i + 1
            break
    left = syms[:split_index]
    right = syms[split_index:]
    
    # Рекурсивное построение кодов для обеих частей
    left_codes = Fano_coding(left)
    right_codes = Fano_coding(right)
    
    # Добавляем '0' к кодам левой части и '1' к кодам правой
    codes = {}
    for symbol, code in left_codes.items():
        codes[symbol] = '0' + code
    for symbol, code in right_codes.items():
        codes[symbol] = '1' + code
    
    return codes

def Entropy(probs):  # вычисление энтропии
    entropy = 0
    for p in probs:
        entropy -= p * math.log2(p)
    return entropy

def average_code_len(codes, freqs, total_symbols):
    avg_length = 0
    for symbol, frequency in freqs.items():
        avg_length += (frequency / total_symbols) * len(codes[symbol])
    return avg_length

def text_analize(text):  # анализ текста с подсчетом всех параметров
    freqs = Counter(text)
    tot_syms = sum(freqs.values())
    
    # Вероятности символов
    probs = {symbol: freq / tot_syms for symbol, freq in freqs.items()}
    
    # Построение кодов Фано
    codes = Fano_coding(list(probs.items()))
    
    # Вычисление энтропии
    entropy = Entropy(probs.values())
    
    # Средняя длина кодов
    avg_len = average_code_len(codes, freqs, tot_syms)
    
    # Оригинальная длина в битах (8 бит на символ)
    original_len = tot_syms * 8
    
    # Длина после кодирования
    compressed_len = tot_syms * avg_len
    
    # Коэффициент сжатия
    compression = original_len / compressed_len
    
    return {
        'frequencies': freqs,
        'codes': codes,
        'entropy': entropy,
        'compression': compression
    }

# Пример использования
text = input("Введите текст: ")
result = text_analize(text)

print("Частоты символов:", result['frequencies'])
print("Коды Фано:", result['codes'])
print("Энтропия:", result['entropy'])
print("Коэффициент сжатия:", result['compression'])
