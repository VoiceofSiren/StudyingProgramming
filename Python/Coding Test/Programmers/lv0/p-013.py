def solution(my_string, is_suffix):
    result = 1
    range_num = min(len(my_string), len(is_suffix))
    for i in range(-1, range_num * (-1) - 1, -1):
        if is_suffix[i] != my_string[i]:
            result = 0
    if len(is_suffix) > len(my_string):
        result = 0
    return result

my_string, is_suffix = input(), input()
print(solution(my_string, is_suffix))

# banana ana
# banana nan
# banana wxyz
# banana abanana