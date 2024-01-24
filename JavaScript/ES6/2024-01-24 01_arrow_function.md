# Arrow Function
<br/>

### 이 글의 목적
    - Arrow Function (화살표 함수)에 대하여 알아보고자 한다.
<br/>

### (Regular) Function
- 일반적으로 사용하는 함수는 두 가지 방법으로 사용될 수 있다.
#### 1. Function Declaration (함수 선언식)
- 함수 선언식은 다음과 같은 특징을 가진다.
#### [특징]
```plaintext
1. 함수 호이스팅 (Hoisting): 함수 선언식으로 작성된 함수는 코드의 최상단으로 끌어올려진 것처럼 동작한다.
                            즉, 함수를 선언하는 코드 이전에 함수를 호출하는 것이 가능하다.
2. 함수의 이름이 반드시 존재해야 한다. 즉, 익명 함수 (Anonymous Function)의 사용이 불가능하다.
```
#### [코드 1-1] - function 정의
```javascript
function addAll(x, y, z) {
    console.log(`${x} ${y} ${z}`);
    return x + y + z;
}
```
#### [코드 1-2] - function 호출
```javascript
console.log(addAll(10, 20, 30));
```
#### [결과 1]
```plaintext
10 20 30
60
```
<br/>

#### 2. Function Expression (함수 표현식)
- 함수 표현식은 다음과 같은 특징을 가진다.
#### [특징]
```plaintext

```
