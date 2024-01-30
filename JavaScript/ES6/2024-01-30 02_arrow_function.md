# Arrow Function
<br/>

### 이 글의 목적
    - Arrow Function (화살표 함수)에 대하여 알아보고자 한다.
    - 이번 글에서는 화살표 함수의 문법뿐만 아니라 더 자세한 내용을 다루고자 한다.
<br/>

### 1. arguments & Parameters
- 일반 함수와 화살표 함수는 arguments와 parameters에서 차이점을 가진다.
#### 1) 일반함수 - arguments
- function 키워드를 사용하여 정의한 일반 함수에는 별도로 정의해주지 않아도 arguments라는 변수를 암묵적으로 전달받는다.
#### [코드 1-1]
```javascript
function main() {
    console.log(arguments)
}
```
#### [코드 1-2]
```javascript
main('12345', 'ABC')
```
#### [결과 1-1]
```plaintext
Arguments(2) ['12345', 'ABC', callee: ƒ, Symbol(Symbol.iterator): ƒ]
```
- arguments는 함수가 전달받은 인자를 담고 있는 배열 형태의 객체이다.
- 따라서, arguments에 인덱스를 통해 접근하여 해당 요소를 조작할 수 있다.
#### [코드 1-3]
```javascript
function main() {
    console.log(arguments[1]);
}
```
#### [코드 1-4]
```javascript
main('12345', 'ABC');
```
#### [결과 1-2]
```plaintext
ABC
```
- arguments 변는 가변 인자의 개수가 정해지지 않은 가변 인자가 전달되는 함수에 쓰이기 적합하다.
<br/>

#### 2) 화살표 함수 - arguments
- 일반 함수와는 달리, 화살표 함수는 arguments라는 변수를 암묵적으로 전달받지 않는다.
#### [코드 2-1]
```javascript
const main = () => {
    console.log(arguments);
}
```
#### [코드 2-2]
```javascript
main('12345', 'ABC');
```
#### [결과 2-1]
```plaintext
Uncaught ReferenceError: arguments is not defined
```
- 그렇다고 해서 화살표 함수가 가변 인자를 전달 받지 못하는 것은 아니다.
#### [코드 2-1]
```javascript
const main = (...params) => {
    console.log(params)
}
```
#### [코드 2-2]
```javascript
main('12345', 'ABC');
```
#### [결과 2]
```plaintext
['12345', 'ABC']
```
