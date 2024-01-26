# Arrow Function
<br/>

### 이 글의 목적
    - Arrow Function (화살표 함수)에 대하여 알아보고자 한다.
<br/>

### 1. (Regular) Function
- 일반적으로 사용하는 함수는 두 가지 방법으로 사용될 수 있다.
#### 1) Function Declaration (함수 선언식)
- 함수 선언식은 다음과 같은 특징을 가진다.
#### [특징]
```plaintext
1. 함수 호이스팅 (Hoisting) 가능: 함수 선언식으로 작성된 함수는 코드의 최상단으로 끌어올려진 것처럼 동작한다.
                            즉, 함수를 선언하는 코드 이전에 함수를 호출하는 것이 가능하다.
2. 함수의 이름이 반드시 존재해야 한다. 즉, 익명 함수 (Anonymous Function)의 사용이 불가능하다.
```
#### [코드 1-1] - function 정의
```javascript
function addAll(x, y, z) {
    console.log(`input: ${x} ${y} ${z}`);
    return x + y + z;
}
```
#### [코드 1-2] - function 호출
```javascript
console.log('output:', addAll(10, 20, 30));
```
#### [결과 1]
```plaintext
input: 10 20 30
output: 60
```
<br/>

#### 2) Function Expression (함수 표현식)
- 함수 표현식은 다음과 같은 특징을 가진다.
#### [특징]
```plaintext
1. 함수 호이스팅 (Hoisting) 불가능: 함수 선언식 이전에 함수를 호출하는 것이 불가능하다
2. 함수의 이름이 반드시 존재하지 않아도 된다. 즉, 익명 함수 (Anonymous Function)의 사용이 가능하다.
```
#### [코드 2-1]
```javascript
const sumFunc = function(x, y, z) {
    console.log(`input: ${x} ${y} ${z}`);
    return x + y + z;
}
```
#### [코드 2-2]
```javascript
console.log('output:', sumFunc(1, 2, 3));
```
#### [결과 2]
```plaintext
input: 1 2 3
output: 6
```
<br/>

### 2. Arrow Function

#### [코드 3-1]
```javascript
const combine = (x, y, z) => {
    console.log(`input: ${x} ${y} ${z}`);
    return x + y + z;
}
```
#### [코드 3-2]
```javascript
console.log('output:', combine(1, 2, 3));
```
#### [결과 3]
```plaintext
input: 1 2 3
output: 6
```
