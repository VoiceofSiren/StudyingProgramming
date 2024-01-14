# Promise

### - Promise 객체를 생성할 경우 파라미터로 두 개의 콜백 함수가 들어가며, <br>내부에 성공 시 실행되는 콜백함수와 실패 시 실행되는 콜백 함수가 들어갈 수 있다. <br>기본적인 코드의 형태는 [코드 1]과 같으며, [코드 1]에서의 Promise의 state와 result는 [상태 1]과 같다. 

#### [코드 1]
	const pr = new Promise ((resolve, reject) => {
		resolve(value);		// resolve: 성공 시 실행되는 함수
		reject(error);		// reject: 실패 시 실행되는 함수
	});

#### [상태 1]
- 생성 시: new Promise

| Property | Value |
|---|---|
| state | pending (대기) |
| result | undefined |

- 성공 시: resolve(value)

| Property | Value |
|---|---|
| state | fulfilled (이행됨) |
| result | value |

- 실패 시: reject(error)

| Property | Value |
|---|---|
| state | rejected (거부됨) |
| result | Error |


### - 성공 시 코드는 아래의 [코드 2]와 같으며, [코드 2]에서의 Promise의 state와 result는 [상태 2]와 같다.
#### [코드 2]
	const pr = new Promise ((resolve, reject) => {
		setTimeout(() => {
			resolve(‘ok’)
		}, 3000)
	});

#### [상태 2]
| Property | Value |
|---|---|
| state | fulfilled (이행됨) |
| result | ‘OK’ |

### - 실패 시 코드는 아래의 [코드 3]과 같으며, [코드 3]에서의 Promise의 state와 result는 [상태 3] 같다.
#### [코드 3]
	const pr = new Promise ((resolve, reject) => {
		setTimeout(() => {
			reject(new Error(‘error’))
		}, 3000)
	});
 
#### [상태 3]
| Property | Value |
|---|---|
| state | rejected (거부됨) |
| result | 'error' |





# fetch API
#### (get more info in https://developer.mozilla.org/en-US/docs/Web/API/fetch)

### - Chrome 브라우저 상에서 F12 키보드를 눌러 개발자 도구를 열고 console에 fetch("API")라고 입력하면 아래와 같은 결과를 얻을 수 있다.

