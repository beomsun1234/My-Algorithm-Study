# 우선순위가 가장 높은 높은 데이터를 가장 먼저 삭제하는 자료구조(힙)

# 최소 힙,최대힙

#삽입시->
# 힙은 로그 n, 삭제시->로그n

import heapq

def heapsort(iterable):
    h=[]
    result= []

    for i in iterable:
        heapq.heappush(h,i)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])


print(result)


###- -----다익스트라 알고리즘 우선순위 큐(힙)을 사용하여 작성

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = 3,4#map(int,input().split()) # 노드수, 간선수

start= 1#int(input()) # 시작 노드
graph = [[]for i in range(n+1)]
distince = [INF]*(n+1)
#for i in range(m):
#    a,b,c = map(int,input().split())
#    graph[a].append((b,c))
#
def dijistra(start):
    q=[]

    heapq.heappush(q,(0,start)) #처음 값, 노드번호
    distince[start] = 0

    while q: #큐가 비어있지아느면
        #가장 최단거리가 짧은 노드에 대한 정보 거내기
        dist, now = heapq.heappop(q) #비용과, 현재 노드 번호
        # 현재 노드가 이미 처리된적이 있는 노드라면 무시
        if distince[now] <dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distince[i[0]]:
                distince[i[0]]= cost
                heapq.heappush(q,cost,i[0])

## 전보: 문제 설명
# 어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우,  다른 도시로 전보를 보내서 다른 도시로
# 해당 메시지를 전송할 수 있다.
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치 되ㅇ어있어야한다
# 통로가 없으면 메시지를 보낼 수 없다. 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소된다(비용)
# 어느날 C라는 도시에서 위급 상황 발생. 그래서 많은 도시에 메시지를 보내고자 한다. 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로르 거쳐 
# 최대한 많이 퍼져나간다
# 각 도시 번호오ㅘ 통로가 설치되오있는 정보가 주어졌을때 , 도시 C에서 보낸 메시지를 받게되는 도시의 개수는 총 몇개 이며, 받는데 까지 걸리는 총 시간을 게산
#c=start a=2  z=
# 
import heapq
import sys
INF = int(1e9)
n,m, c = map(int,input().split())

graph = [[]for i in range(n+1)]
distince = [INF]*(n+1)
start = c
#z=비용, y=연결된 노드
for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))


print(graph)
cnt=0

def djic(start):
    q=[]
    heapq.heappush(q,(0,start))
    distince[start]=0

    while q:
        dist, now = heapq.heappop(q)
        if distince[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost <distince[i[0]]:
                distince[i[0]]= cost
                heapq.heappush(q,(cost,i[0]))


            

djic(start)
sum=0
for i in range(n):
    if distince[i]!=INF:
        cnt+=1
        print(i)
        print(distince[i])

print(cnt, sum)

#### 미래도시 
#1 번 부터 n번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어있다.
# 방문판매원 a는 현재 1번 회사에 위치해있으며, x번 회사에 방문해 물건을 판매하고자한다.









