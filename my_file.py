import random

def analyse():
    pval = random.random()
    return pval

def is_valid(pval):
    if pval < 0.05:
        return True
    else:
        return False

result = analyse()
print(result, is_valid(result))
