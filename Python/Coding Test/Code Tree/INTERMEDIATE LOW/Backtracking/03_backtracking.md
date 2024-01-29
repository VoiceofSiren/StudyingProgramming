# Backtracking
###### Question: https://www.codetree.ai/missions/2/problems/yutnori-1d?&utm_source=clipboard&utm_medium=text
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
n, m, k = tuple(map(int, input().split()))

# 총 n번에 걸친 턴들
turn_list = list(map(int, input().split()))

# k개의 말 - 기본적으로 1에서 시작하므로 각 말들의 기본값을 1로 설정
entity_list = [ 1 for _ in range(k) ]

# 정답
answer = 0
```
#### [코드 1-2]
```python
def calculate_score():
    score = 0
    # 각 말들에 대하여 m보다 크면 점수에 1씩 더해주기
    for entity in entity_list:
        if entity >= m:
            score += 1
    return score
```
#### [코드 1-3]
```python
def get_max_score(current_turn):
    global answer

    answer = max(answer, calculate_score())

    if current_turn == n:
        return

    for i in range(k):
        if entity_list[i] >= m:
            continue
        
        entity_list[i] += turn_list[current_turn]
        get_max_score(current_turn + 1)
        entity_list[i] -= turn_list[current_turn]
```
#### [코드 1-4]
```python
get_max_score(0)
print(answer)
```
#### [결과 1]
```plaintext
2
```
#### --> 정답이 도출되었다.
