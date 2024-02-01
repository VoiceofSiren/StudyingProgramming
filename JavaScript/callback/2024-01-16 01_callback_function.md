# Callback Function
<br/>

### 이 글의 목적
    - JavaScript에서 자주 사용되는 Callback Function의 개념과 쓰임새에 대해 알아보고자 한다.
<br/>

### Callback Function
    - 다른 함수의 인자로 전달되는 함수.
    - 주로 비동기 작업을 처리할 때 사용된다.
#### Callback 함수의 원리와 사용법에 대해서는 아래의 특징 1, 2, 3에 의해 정해진다.

<br><br>

### 1. 함수는 값이 될 수 있다.
#### JavaScript에서는 함수 자체가 값이 될 수 있다. 즉, 함수를 변수에 할당할 수 있다.
#### 더 정확히 말하자면, 변수가 함수를 가리키도록 할 수 있다.
#### [코드 1]은 변수 x가 함수를 가리키는 예시이다.
#### [코드 1]
```javascript
x = function() {
  return 5;
}
```
<br/>

### 2. 함수는 반환 값이 될 수 있다.
#### JavaScript에서는 함수가 함수를 반환할 수 있다. 즉, 함수가 다른 함수의 반환 값이 될 수 있다.
#### [코드 2]에서는 x가 함수를 가리키고 있으며, 그 x를 func() 함수가 반환한다.
#### [코드 2]
```javascript
function func() {
  x = function() {
      return 5;
  }
  return x;
}
```
<br/>

### 3. 함수는 인자가 될 수 있다.
#### JavaScript에서는 함수의 인자로 함수가 들어갈 수 있다.
#### [코드 3]에서는 func(x)가 호출되었을 때 함수를 가리키는 x가 func() 함수의 인자로 들어가 실행된다.
#### [코드 3]을 실행하면 [결과 1]이 정상적으로 출력된다.
#### [코드 3]
```javascript
x = function() {
    console.log(5);
}
function func(y) {
    y();
}
func(x);
```
#### [결과 1]
```plaintext
5
```
<br/>

#### --> 결과적으로 [코드 3]에서 함수 x는 사전에 정의되어 있지만 func(x)가 호출될 때 사후에 함수 x가 호출된다는 점에서,
#### x를 Callback Function (콜백 함수)이라고 한다.













