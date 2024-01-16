# Spread Operators
<br/>

### Spread Operators
    - Iterable elements (반복 가능한 요소)들에 적용할 수 있는 문법.
    - 배열이나 문자열 등에 ...을 붙여 사용된다.
<br/>

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
<br/>

#### 다만, [코드 2-4]처럼 코드를 작성하려는 경우 유의해야 한다.
#### [코드 2-4]
```plaintext
const str3 = ...str1;
```
#### [결과 2-4]
    TypeError: spread argument must have iterable type
#### --> Spread operators는 배열이나 객체의 요소를 확장하는 데 사용되므로, 문자열 자체로는 iterable하지 않음을 시사한다.
<br/>

### 3. 배열에 배열을 덧붙이기
#### [코드 3-1] - 배열의 마지막에 첨부
```plaintext
const numbers1 = [30, 8, ...arr];
console.log(numbers1);
```
#### [결과 3-1]
    [30, 8, 1, 2, 4, 6]
---
#### [코드 3-2] - 배열의 중간에 삽입
```plaintext
const numbers2 = [30, ...arr, 8];
console.log(numbers2);
```
#### [결과 3-2]
    [30, 1, 2, 4, 6, 8]
---
#### [코드 3-3] - 배열의 처음에 첨부
```plaintext
const numbers3 = [...arr, 30, 8];
console.log(numbers3);
```
#### [결과 3-3]
    [1, 2, 4, 6, 30, 8]
#### --> 배열의 index에 관계없이 배열이 잘 덧붙여지는 것을 확인할 수 있다.


### 4. 배열을 복사하기
#### [코드 4]
```plaintext
const copiedArr = [...arr];
console.log(copiedArr);
```
#### [결과 4]
    [1, 2, 4, 6]
#### --> [결과 4]를 통해 배열이 정상적으로 복사되었음을 확인할 수 있다.
####      다만, 이 복사 방법은 Shallow Copy가 아니라 Deep Copy이므로, 새로운 배열을 만들어 이 배열에 값만 그대로 복사해온 것과 같다.
#### 즉, 복사한 이후에 arr의 내용이 바뀐다고 해서 copiedArr의 내용도 따라서 바뀌지는 않는다.



