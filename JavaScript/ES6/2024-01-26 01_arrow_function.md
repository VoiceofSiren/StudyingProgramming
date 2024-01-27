# Arrow Function
<br/>

### 이 글의 목적
    - Arrow Function (화살표 함수)에 대하여 알아보고자 한다.
    - 이번 글에서는 화살표 함수의 기본적인 문법에 대해서만 이해할 것이며,
      더 자세한 내용은 추후 새로운 글을 작성하면서 알아볼 예정이다.
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
- function 키워드 대신 화살표 (=>)를 사용하여 화살표 함수를 정의할 수 있다.
#### 1) 기본적인 화살표 함수의 문법
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
#### 2) 화살표 함수의 변형
- [코드 4-1]처럼 매개변수가 한 개이고 {}블록 내부에 한 줄의 코드만 있는 Arrow Function이 있다고 가정하자.
- [결과 4]는 [코드 4-1]과 [코드 4-2]에 대한 출력 결과이다.
#### [코드 4-1]
```javascript
const getFirstElement = (arr) => {
    return arr[0];
}
```
#### [코드 4-2]
```javascript
numArr = [50, 51, 52, 53]
console.log(getFirstElement(numArr));
```
#### [결과 4]
```plaintext
50
```
- [코드 4-1]처럼 작성된 코드는 [코드 5-1]처럼 형태를 간략화하여 작성될 수 있다.
#### [코드 5-1]
```javascript
const getFirstElement = arr => arr[0]
```
#### [코드 5-2]
```javascript
numArr = [50, 51, 52, 53]
console.log(getFirstElement(numArr));
```
#### [결과 5]
```plaintext
50
```
#### --> [코드 4-1]과 [코드 4-2]에 대한 결과와 [코드 5-1]과 [코드 5-2]에 대한 결과가 일치함을 확인할 수 있다.
- 다만, JavaScript Object를 return하는 Arrow Function의 경우 중괄호가 문법의 혼란을 야기할 수 있으므로, 반드시 [코드 6]에서처럼 JavaScript Object를 소괄호로 감싸주어야 한다.
#### [코드 6]
```javascript
const getJSObject = () => ({"key": "value"})
```
