## news crawling

### 현재 프로그램의 제한/추가 기능 필요사항

#### 1. 현재 2개의 thread 로 작업 진행
#### - 그중 crawling 을 하는 thread 의 작업시간이 매우 길기 때문에 thread pool 로 작업해야 할듯
#### 2. MongoDB 의 찾기 기능이 find_one 만 제대로 작동한다. 따라서 실제 동일한 시간에 crawling 요청되 다수의 db 요청처리가 불가한 상태
#### 3. keyword 마다 파일을 하나씩 만들고 각각 메일을 보내고 있는 상태, 따라서 다수의 keyword 를 가진 계정에는 메일이 비효율적으로 발생되고 있음.

