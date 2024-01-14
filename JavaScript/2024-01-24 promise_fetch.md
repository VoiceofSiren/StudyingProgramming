# Promise

## Promise 객체를 생성할 경우 파라미터로 콜백 함수가 들어가며, 일반적으로 아래와 같이 사용된다.

	const pr = new Promise ((resolve, reject) => {
		// resolve: 성공 시 실행되는 함수
		// reject: 실패 시 실행되는 함수
	});

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





# fetch API
### (get more info in https://developer.mozilla.org/en-US/docs/Web/API/fetch)

## Chrome 브라우저 상에서 F12 키보드를 눌러 개발자 도구를 열고 console에 fetch("API")라고 입력하면 아래와 같은 결과를 얻을 수 있다.
