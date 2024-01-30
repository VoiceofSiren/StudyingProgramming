# Destructuring Assignment
<br/>

### 이 글의 목적
    - ES6부터 도입된 Destructuring Assignment (구조 분해 할당)에 대해 알아보고자 한다.
<br/>

### Destructuring Assignment
- 객체나 배열의 속성을 쉽게 추출하여 변수에 할당할 수 있게 해주는 기능.
#### 1) 기존의 문법
- 객체나 배열의 속성을 개별적으로 변수에 할당해야 했다.
- 이 때문에 반복문을 사용하거나 [코드 1]에서처럼 여러 줄의 코드를 작성해야만 했다.
#### [코드 1]
```javascript
        let numArr = [100, 200, 300, 400];

        let e1 = numArr[0];
        let e2 = numArr[1];
        let e3 = numArr[2];
        let e4 = numArr[3];
```
#### 2) Destructuring Assignment

