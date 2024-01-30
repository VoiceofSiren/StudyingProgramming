# Destructuring Assignment
<br/>

### 이 글의 목적
    - ES6부터 도입된 Destructuring Assignment (구조 분해 할당)에 대해 알아보고자 한다.
<br/>

### 1. Destructuring Assignment
- 객체나 배열의 속성을 쉽게 추출하여 변수에 할당할 수 있게 해주는 기능.
- 이번 글에서는 배열에 구조 분해 할당을 적용하는 방법에 대해서 알아볼 것이다.
<br/>

### 2. 기존의 문법
- 배열의 속성을 개별적으로 변수에 할당해야 했다.
- 이 때문에 반복문을 사용하거나 [코드 1]에서처럼 여러 줄의 코드를 작성해야만 했다.
#### [코드 1]
```javascript
let numArr = [100, 200, 300, 400];

let e1 = numArr[0];
let e2 = numArr[1];
let e3 = numArr[2];
let e4 = numArr[3];
```
<br/>

### 3. Destructuring Assignment (배열)
- [코드 1]에서는 n개의 변수에 값을 할당하기 위해 n줄의 변수 초기화문을 사용해야 했지만, Destructuring Assignment를 사용하면 [코드 2]에서처럼 한 줄로 할당할 수 있다.
#### [코드 2-1]
```javascript
let numArr = [100, 200, 300, 400];

let [e1, e2, e3, e4] = numArr;
```
- 배열의 일부 요소만 할당하고 싶을 경우, [코드 3]에서처럼 할당하고 싶은 값에 해당하는 인덱스에만 변수를 할당해주면 된다.
#### [코드 2-2]
```javascript
    let numArr = [100, 200, 300, 400];
    let [n1, , n3, ] = numArr;
    console.log(`n1 = ${n1}, n3 = ${n3}`);
```
#### [결과 1]
```plaintext
n1 = 100, n3 = 300
```
- Destructuring Assginment에 Spread Operators를 적용하는 것도 가능하다.
- [코드 3]은 numArr 배열의 모든 요소를 배열의 형태로 할당받는 방식이다.
#### [코드 3]
```javascript
let numArr = [100, 200, 300, 400];
let [...newArr] = numArr;
console.log(newArr);
```
#### [결과 2]
```plaintext
[100, 200, 300, 400]
```
- [코드 4]는 numArr의 앞부분에 있는 연속한 요소들을 별도의 변수로 먼저 할당시키고 나머지 요소를 Spread Operators를 사용해서 할당시키는 방식이다.
#### [코드 4]
```javascript
let numArr = [100, 200, 300, 400];
let [x, y, ...newArr] = numArr;
console.log(`x = ${x}, y = ${y}, newArr = ${newArr}`);
```
#### [결과 3]
```plaintext
x = 100, y = 200, newArr = 300,400
```
