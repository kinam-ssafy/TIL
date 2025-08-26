### Collections 라이브러리

`collections`는 파이썬의 표준 라이브러리로, 일반적인 내장 데이터 타입(`list`, `dict`, `tuple` 등)을 보완하는 **고성능 컨테이너**를 제공. 특정 작업에 최적화된 자료 구조를 통해 코드의 효율성과 가독성을 높이는 데 도움을 줌.

-----

### Deque (데크)

`deque`는 **Double-Ended Queue**의 줄임말로, 양쪽 끝에서 데이터를 빠르게 추가하거나 삭제할 수 있는 자료 구조. 리스트보다 큐와 스택 구현에 훨씬 효율적임.

#### 주요 메서드와 코드 예시

  * **`append(x)`**
      * 덱의 오른쪽에 `x`를 추가.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([1, 2, 3])
    queue.append(4)
    # deque([1, 2, 3, 4])
    ```
  * **`appendleft(x)`**
      * 덱의 왼쪽에 `x`를 추가. 이 연산은 O(1) 시간 복잡도로 매우 빠름.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([1, 2, 3])
    queue.appendleft(0)
    # deque([0, 1, 2, 3])
    ```
  * **`pop()`**
      * 덱의 오른쪽 끝에서 요소를 제거하고 반환.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([1, 2, 3])
    item = queue.pop()
    # item: 3, queue: deque([1, 2])
    ```
  * **`popleft()`**
      * 덱의 왼쪽 끝에서 요소를 제거하고 반환. 큐의 핵심 연산으로, O(1) 시간 복잡도를 가짐.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([1, 2, 3])
    item = queue.popleft()
    # item: 1, queue: deque([2, 3])
    ```
  * **`extend(iterable)`**
      * iterable의 모든 요소를 덱의 오른쪽에 추가.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([1, 2])
    queue.extend([3, 4])
    # deque([1, 2, 3, 4])
    ```
  * **`extendleft(iterable)`**
      * iterable의 모든 요소를 덱의 왼쪽에 역순으로 추가.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([3, 4])
    queue.extendleft([1, 2])
    # deque([2, 1, 3, 4])
    ```
  * **`rotate(n)`**
      * 덱의 요소를 `n`만큼 회전. 양수 `n`은 오른쪽, 음수 `n`은 왼쪽으로 회전.
    <!-- end list -->
    ```python
    from collections import deque
    queue = deque([1, 2, 3, 4])
    queue.rotate(1)
    # deque([4, 1, 2, 3])
    queue.rotate(-1)
    # deque([1, 2, 3, 4])
    ```

-----

#### 활용 사례

  * **큐(Queue)**: `append()`와 `popleft()`를 이용해 FIFO(선입선출) 구조를 구현. BFS(너비 우선 탐색)에 사용.
  * **스택(Stack)**: `append()`와 `pop()`을 이용해 LIFO(후입선출) 구조를 구현.
  * **슬라이딩 윈도우**: `maxlen` 인자를 사용하여 덱의 크기를 고정하면, 최근 N개의 데이터만 유지하는 자료 구조를 만들 수 있음.