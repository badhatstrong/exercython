def score(x, y):
    result = 0
    if pow(x, 2) + pow(y, 2) <= 1:
        result = 10
    elif pow(x, 2) + pow(y, 2) <= 25:
        result = 5
    elif pow(x, 2) + pow(y, 2) <= 100:
        result = 1
    else:
        result = 0
    return result

