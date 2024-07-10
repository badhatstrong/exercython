def score(x: int, y:int) -> int:
    result = 0
    circle_checkout: int = x ** 2 + y ** 2
    if circle_checkout <= 1:
        result = 10
    elif circle_checkout <= 25:
        result = 5
    elif circle_checkout <= 100:
        result = 1
    return result

