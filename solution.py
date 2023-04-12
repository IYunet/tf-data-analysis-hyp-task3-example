import pandas as pd
import numpy as np
import statsmodels.stats.weightstats as weight


chat_id = 426527714

def solution(x: np.array) -> bool:
    alfa = 0.04
    threshold = 500
    a, pvalue = weight.ztest(x, value=500, alternative='larger')
    return pvalue <= alfa
