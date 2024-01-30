# Destructuring Assignment
<br/>

### 이 글의 목적
    - ES6부터 도입된 Destructuring Assignment (구조 분해 할당)에 대해 알아보고자 한다.
<br/>

### 1. Destructuring Assignment
- 객체나 배열의 속성을 쉽게 추출하여 변수에 할당할 수 있게 해주는 기능.
- 이번 글에서는 객체에 구조 분해 할당을 적용하는 방법에 대해서 알아볼 것이다.
<br/>

### 2. 기존의 문법
- 객의 속성을 개별적으로 변수에 할당해야 했다.
- 이 때문에 반복문을 사용하거나 [코드 1]에서처럼 여러 줄의 코드를 작성해야만 했다.
#### [코드 1]
```javascript
let operators = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/"
}

let add = operators['add'];
let subtract = operators.subtract;
let multiply = operators.multiply;
let divide = operators['divide'];
```
<br/>

### 3. Destructuring Assignment (객체)
- [코드 1]에서는 n개의 변수에 값을 할당하기 위해 n줄의 변수 초기화문을 사용해야 했지만, Destructuring Assignment를 사용하면 [코드 2]에서처럼 한 줄로 할당할 수 있다.
#### [코드 2-1]
```javascript
let operators = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/"
}

let {add, subtract, multiply, divide} = operators;
```
- 객체의 key 중 일부만 변수로 할당하고 싶을 경우 [코드 2-2]처럼 작성하면 된다.
#### [코드 2-2]
```javascript
let {add, subtract} = operators;
console.log(`add = ${add}, subtract = ${subtract}`);
```
#### [결과 1-1]
```plaintext
add = +, subtract = -
```
- 객체의 key의 이름을 변경하여 변수로 할당하고 싶은 경우 [코드 2-3]처럼 작성하면 된다.
#### [코드 2-3]
```javascript
let {add: sum, subtract: cut_out} = operators;
console.log(`sum = ${sum}, cut_out = ${cut_out}`);
```
#### [결과 1-2]
```plaintext
sum = +, cut_out = -
```
