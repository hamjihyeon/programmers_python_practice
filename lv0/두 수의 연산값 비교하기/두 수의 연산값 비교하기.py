def solution(a, b):
    str_add = str(a) + str(b)
    if int(str_add) >= 2 * a * b:
        return int(str_add)
    else:
        return (2 * a * b)