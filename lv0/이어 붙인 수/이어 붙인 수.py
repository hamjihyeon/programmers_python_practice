def solution(num_list):
    add_even = ''
    add_odd = ''
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            add_even += str(num_list[i])
        else:
            add_odd += str(num_list[i])
    return int(add_even) + int(add_odd)