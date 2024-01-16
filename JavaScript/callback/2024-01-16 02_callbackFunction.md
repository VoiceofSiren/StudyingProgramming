# Callback Function
<br/>

### 이 글의 목적
    - callback/2024-01-16 01_callbackFunction.md에서 callback function의 개념을 위주로 학습하였다.
    - 이번 글을 통해 구체적인 예시를 제시하여 콜백 함수를 잘 활용할 수 있도록 하겠다. 
<br/>

### Array.prototype.filter() API
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter에서 확인 가능.
    - 아래의 예제 코드인 [코드 1]을 통해 콜백 함수의 원리를 더 깊게 이해해보도록 하자.
    - [코드 1]은 주어진 문자열을 요소로 가지는 배열에 대하여 각 요소의 길이가 6보다 큰 문자열들만 필터링하여 console에 출력하는 코드이다.
#### [결과 1]은 [코드 1]을 실행했을 때 console에 출력되는 결과이다.

#### [코드 1]
```plaintext
const words = ['spray', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter((word) => word.length > 6);
console.log(result);
```
#### [결과 1]
    ['exuberant', 'destruction', 'present']
#### --> [결과 1]에서 문자열의 길이가 6을 초과하는 요소만 잘 필터링되었음을 확인할 수 있다.
<br/>

#### 예제 코드인 [코드 1]을 [코드 2]처럼 변형해 보았다.
#### [결과 2]는 [코드 2]를 실행했을 때 console에 출력되는 결과이다.
#### [코드 2]
```plaintext
const words = ['spray', 'elite', 'exuberant', 'destruction', 'present'];
const wordFunc = function (word) {
    return word.length > 6;
};
const result2 = words.filter(wordFunc);
console.log(result2);
```
#### [결과 2]
    ['exuberant', 'destruction', 'present']
#### --> [결과 1]과 [결과 2]를 통해 알 수 있듯이, 동일한 배열이 출력되었음을 확인할 수 있다.

#### --> 결과적으로, [코드 1]의 (word) => word.length > 6 이 부분이 콜백 함수임을 알 수 있다.




