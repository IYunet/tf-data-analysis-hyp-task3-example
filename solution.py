import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 426527714

def solution(x: np.array) -> bool:
    alpha = 0.04
    threshold = 500
    t_statistic, p_value = ttest_1samp(x, threshold)
    return p_value < alpha and t_statistic > 0
