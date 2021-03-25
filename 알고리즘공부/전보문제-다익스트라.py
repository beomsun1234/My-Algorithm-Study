


import heapq
import sys
inpurt = sys.stdin.readline
INF = int(1e9)

#n은 노드에 개수, m은 간선의 개수
n,m = map(int,input().split())
graph = [[]for i in range(n+1)] 

distince = [INF]*(n+1)


start = 1

print(start)
# b는 간선 , c는 비용
for i in range(m):
    a, b= map(int,input().split())
    graph[a].append((b,1))


def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distince[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distince[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distince[i[0]]:
                distince[i[0]]= cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
d=0
for i in range(n+1):
    if distince[i]!=INF:
        d=max(distince[i],d)

print(d)
