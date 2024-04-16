'''
https://school.programmers.co.kr/learn/courses/30/lessons/181916
'''

def solution(a, b, c, d):
    abcd = {a, b, c, d}
    if len(abcd) == 1:
        p = a
        return 1111 * p
    elif len(abcd) == 4:
        return min(abcd)
    else:
        if len(abcd) == 2:  # 3+1 또는 2+2
            abcd = sorted([a, b, c, d])
            return judge_duplicates2(abcd)
        else:               # 2+1+1
            abcd = sorted([a, b, c, d])
            p, q, r = judge_duplicates3(abcd)
            return q * r

def judge_duplicates2(num_list):
    a, b, c, d = num_list
    if a == b and c == d:
        return (a + c)*abs(a - c)
    elif b == c and a == d:
        return (b + a)*abs(b - a)
    elif c == d and a == b:
        return (c + a)*abs(c - a)
    elif a==b==c:
        return (10*a + d)**2
    elif a==b==d:
        return (10*a + c)**2
    elif b==c==d:
        return (10*b + a)**2

def judge_duplicates3(num_list):
    a, b, c, d = num_list
    if a == b and c != d:
        return a, c ,d
    elif b == c and a != d:
        return b, a, d
    elif c == d and a != b:
        return c, a, b

a, b, c, d = map(int, input().split())
print(solution(a, b, c, d))

# 2 2 2 2
# 4 1 4 4
# 6 3 3 6
# 2 5 2 6
# 6 4 2 5