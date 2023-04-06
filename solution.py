import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    koef = 2/(56*56)
    alpha = 1 - p
    quan_1 = gamma(len(x), 1).ppf((1-alpha)/2)
    quan_2 = gamma(len(x), 1).ppf((1+alpha)/2)
    sum = np.sum(x)
    return (koef*((quan_1+sum)/2)-1/2, koef*((quan_2+sum)/2)-1/2)
