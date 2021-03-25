#### 미래도시 
#1 번 부터 n번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어있다.
# 방문판매원 a는 현재 1번 회사에 위치해있으며, x번 회사에 방문해 물건을 판매하고자한다.

import heapq
n,m= map(int,input().split())
start = 1
graph = [[]for i in range(n+1)]
INF=int(10e9)
distince=[INF]*(n+1)

#a= 노드, b= 다음 노드  c=1 (비용)
for i in range(m):
    a,b= map(int, input().split())
    graph[a].append((b,1))

k,x=map(int,input().split())
print(graph)


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
for i in range(n+1):
    if distince[i]!=INF:
        print(i,'=',distince[i])

if distince[k] ==INF or distince[x] ==INF:
    print(-1)
else:
    print(distince[k]+distince[x])