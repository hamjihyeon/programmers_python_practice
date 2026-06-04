def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    return int(max(str_a + str_b, str_b + str_a))