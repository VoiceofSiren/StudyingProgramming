# Spread Operators
<br/>

### Spread Operators
    - Iterable elements (반복 가능한 요소)들에 적용할 수 있는 문법.
    - 배열이나 문자열 등에 쓰인다.

### 1. 배열의 모든 요소를 순차적으로 출력하기
#### [코드 1]
```plaintext
    const arr = [1, 2, 4, 6];
    console.log(...arr);
```
#### [결과 1]
    1 2 4 6
<br/>

### 2. 문자열의 모든 요소를 순차적으로 출력하기
#### [코드 2-1]
```plaintext
    const str1 = 'hello';
    console.log(str1);
```
#### [결과 2-1]
    hello
---
#### [코드 2-2]
```plaintext
    const str2 = [...str1];
    console.log(str2);
```
#### [결과 2-2]
    ['h', 'e', 'l', 'l', 'o']
<br/>
