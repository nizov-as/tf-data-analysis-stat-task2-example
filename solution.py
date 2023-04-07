import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    left_i = 2/(56*56) * (gamma.ppf((1-p)/2, x.size)/x.size+x.mean()-1/2)
    right_i = 2/(56*56) * (gamma.ppf((1+p)/2, x.size)/x.size+x.mean()-1/2)
    return left_i, right_i
