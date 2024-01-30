# Spread Operators
</br>

### 이 글의 목적
    - ES6/2024-01-16 01_spreadOperators.md에서 Spread Operators를 생성하고 다른 배열에 확장시키거나 복사하는 방법에 대해 학습하였다.
    - Spread Operators는 함수의 인자로서 사용되는 경우가 비일비재하므로, 정확한 사용법이 무엇인지 이 글을 통해 알아볼 것이다.
</br>

### 1. 함수의 전달
#### 아래의 [코드 1-2]는 함수의 argument로 배열이 들어갈 때 Spread Operator를 사용하여 각각의 요소를 꺼내오는 방법을 보여주고 있다.
#### [코드 1-1]
```javascript
function sum(a, b, c, d) {
    return a + b + c + d;
}
```
#### [코드 1-2]
```javascript
const numArr = [1, 2, 3, 4];

console.log(sum(...numArr));
console.log(sum(100, ...numArr));
```
#### [결과 1]
```plaintext
10
106
```
#### --> JavaScript에서 사실 매개변수의 중요도는 낮은 편이다.
#### 따라서, [코드 1-2]에서 sum(100, ...numArr)처럼 호출해도 sum()의 인자로 100, 1, 2, 3까지만 들어가고 4는 버려진다.
<br/>

### 2. 함수의 가변적 매개변수 사용
#### 함수를 정의할 때 크기가 가변적인 매개변수로서 활용할 수 있으며,
#### 이 경우 Spread Operator를 사용한 파라미터는 반드시 마지막에 위치해 있어야 한다.
#### [코드 2-1]
```javascript
function combineFunc(obj, ...arr) {
    return [obj, ...arr];
}
```
#### [코드 2-2]
```javascript
console.log(combineFunc({"one": 1, "two": 2}, 3, 4));
console.log(combineFunc({"one": 1, "two": 2}, 3, 4, 5, 6));
```
#### [결과 2]
```plaintext
[{"one": 1, "two": 2}, 3, 4]
[{"one": 1, "two": 2}, 3, 4, 5, 6]
```
#### --> 이 방법은 파라미터의 개수를 가변적으로 하고 싶을 때 사용하면 좋다.
<br/>

