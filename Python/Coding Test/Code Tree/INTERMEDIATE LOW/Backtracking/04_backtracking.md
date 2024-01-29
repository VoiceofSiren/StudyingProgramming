# Backtracking
###### Question: https://www.codetree.ai/missions/2/problems/max-of-xor?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - Backtracking 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 윷놀이 게임 중 각 턴을 돌리면서 나올 수 있는 최대 점수를 출력해야 한다.
- 각 말들이 이동하면서 각 말들에 이동할 칸의 값을 더하여 윷놀이 판의 길이보다 크거나 같은지를 비교한다.
#### [코드 1-1]
```python
n, m = tuple(map(int, input().split()))

'''
2, 4, 5 -> 010 100 101 -> 110 101 -> 011
1, 3, 5 -> 001 010 100 -> 011 100 -> 111
'''

num_list = list(map(int, input().split()))
arr = []


def make_binary(num):
    binary_list = [0 for _ in range(20)]
    idx = 19
    while num > 0:
        binary_list[idx] = (num % 2)
        num = (num // 2)
        idx -= 1
    return binary_list

def make_binary_all(num_list):
    for num in num_list:
        arr.append(make_binary(num))

make_binary_all(num_list)
for row in arr:
    print(row)
```
#### [결과 1]
```plaintext
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
```
#### --> 각각의 입력된 숫자에 대해서 이진수 배열이 잘 만들어졌음을 확인할 수 있다.
<br/>

