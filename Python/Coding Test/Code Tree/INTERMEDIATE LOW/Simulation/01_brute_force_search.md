# dx dy technique
###### Question: https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >

#### [코드 1]
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]

def count_coins(i, j, square):
    count_value = 0
    for i in range(i, i+3):
        for j in range(j, j+3):
            if square[i][j] == 1:
                count_value += 1
    return count_value


max_value = 0
for i in range(n-2):
    for j in range(n-2):
        coin_value = count_coins(i, j, square)
        if coin_value > max_value:
            max_value = coin_value
print(max_value)
