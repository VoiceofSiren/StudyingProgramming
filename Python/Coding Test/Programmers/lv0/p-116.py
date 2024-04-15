'''
https://school.programmers.co.kr/learn/courses/30/lessons/181836
'''

def solution(picture, k):
    answer = []
    for p in picture:
        for i in range(k):
            pic = ''
            for j in range(len(p)):
                pic += p[j] * k
            answer.append(pic)
    return answer

picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2
print(solution(picture, k))

'''
[.xx...xx., x..x.x..x, x...x...x, .x.....x., ..x...x.., ...x.x..., ....x....]
2
'''
'''
[x.x, .x., x.x]
3
'''