#스택 구현 라스트인 퍼스트아웃

stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
print(stack[::-1]) ##최상단 원소부터 출력
print(stack)# 최하ㅏ단원소부터출력



##큐구현 퍼스트인 퍼스트아웃
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() ## 큐 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print("먼저들어온 순서",queue) # 먼저들어온 순서대로 출력
queue.reverse() ## 역순으로 바꾸기
print("역순",queue)