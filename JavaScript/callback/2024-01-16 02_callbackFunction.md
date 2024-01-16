# Callback Function
<br/>

### 이 글의 목적
    - callback/2024-01-16 01_callbackFunction.md에서 callback function의 개념을 위주로 학습하였다.
    - 이번 글을 통해 구체적인 예시를 제시하여 콜백 함수를 잘 활용할 수 있도록 하겠다. 
<br/>


### Array.prototype.filter() API
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter에서 확인 가능.
    - 아래의 예제 코드 [코드 1]을 통해 콜백 함수의 원리를 더 깊게 이해해보도록 하자.

#### [코드 1]
```plaintext
    const words = ['spray', 'elite', 'exuberant', 'destruction', 'present'];
    const result = words.filter((word) => word.length > 6);
    console.log(result);
```


















