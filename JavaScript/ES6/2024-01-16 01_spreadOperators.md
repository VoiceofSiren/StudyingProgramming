# Spread Operators
<br/>

### Spread Operators
    - Iterable elements (반복 가능한 요소)들에 적용할 수 있는 문법.
    - 배열이나 문자열 등에 ...을 붙여 사용된다.

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
---
#### [코드 2-3]
```plaintext
    console.log(...str1);
```
#### [결과 2-3]
    h e l l o

#### 다만, [코드 2-4]처럼 코드를 작성하려는 경우 유의해야 한다.
#### [코드 2-4]
```plaintext
    const str3 = ...str1;
```
#### [결과 2-4]
    TypeError: spread argument must have iterable type
#### --> Spread operators는 배열이나 객체의 요소를 확장하는 데 사용되므로, 문자열 자체로는 iterable하지 않음을 시사한다.
<br/>
