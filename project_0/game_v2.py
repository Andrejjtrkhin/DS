"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binarySearch(number: int = 1) -> int:
    count = 0
    
    predict_number = 50
    minNum = 1
    maxNum = 101
    
    while(number != predict_number):
        count += 1
        if number > predict_number:
            minNum = predict_number
            predict_number = (minNum + maxNum) // 2
        else:
            maxNum = predict_number
            predict_number = (minNum + maxNum) // 2
    return count


def binarySearch_2(number: int = 1) -> int:
    count = 0
    
    predict_number = 50
    
    while(number != predict_number):
        count += 1
        if number > predict_number:
            predict_number = np.random.randint(predict_number, 101) 
        else:
            predict_number = np.random.randint(1, predict_number) 
    return count

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binarySearch_2)
