##서로소 집합 자료구조

# 서로소란 공통원소가 없는 두 집합을 의미
#서로소 집합 자료구조는 두종료의 연산을 지원
# 1. 합집합: 두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# 2. 찾기: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

# 서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라고 불리기도한다

## 동작 과정-
# 1. 합집합 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인합니다.
#    1) A와 B의 루트노드 A`, B`를 각각 찾습니다.
#    2) A`를 B`의 부모 노드로 설정합니다

# 2. 모든 합집합 연산을 처리할때까지 1번의 과정을 반복

# ex  union(1,4), Union(2,3), Union(2,4), Union(5,6)
# 처음 노드에 부모를 자기 자신으로 설정
# 다음 유니온할때 현재 루트노드를 비교하여 1,4의 부모 노드를 비교하여 부모 노드가 더 큰 번호(4)에 해당하는 루트노드의 부모를 작은 부모노드 값으로로 변경

#-----------------------------
# 기본적인 구혀 방법

# 특정원소가 속하는 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x]!=x: ##parent= 부모테이블  x= 노드 번호 , 현재 부모가 자기 자신이 아니라면(루트가 아님), 
        return find_parent(parent,parent[x]) #루트를 찾기위해 자기에 부모노드를 넣음으로써 찾음

    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b:
        parent[b]=a

    else:
        parent[a]=b

# 노드의 개수와 간선(유니온 연산)의 개수 입력받기
v,e= map(int,input().split())

parent=[0]*(v+1) #부모테이블 초기화

#부모테이블을 자기 자신으로 초기화

for i in range(1,v+1):
    parent[i]=i


#유니온 연산 을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b) # 서로 연결하는것


print("각원소가 속한 집합:", end='')
# 각원소의 속한 집합출력
for i in range(1,v+1):
    print(find_parent(parent,i),end='')

print()


print('부모 테이블:', end='  ')
for i in range(1,v+1):
    print(parent[i], end=' ')



################

# 서로소 집합 자료구조: 경로 압축

# 찾기 함수를 최적화하기 위한 방법으로 경로 압축 을 이용할 수 있다.
#  찾기 함수를 재귀적으로 호출한뒤에 부모테이블값을 바로 갱신

def find_parent_path_compression(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent_path_compression(parent,parent[x])
    return parent[x]




## 서로소 집합을 활용한 사이클 판별
# 참고로 방향그래프에서 사이클 여부는 dfs를 이요ㅕㅇ하여 판별할수 있습니다.
# 
# 사이클 판별 알고리즘이란?
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다
#  1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(유니온)연산을 수행.
#  2) 루트 노드가 서로 같다면 사이클이 발생한 것
# 
# 2. 그래프에 포함되어 있는 모든 간선에 대하여 1 번과정을 반복   


#알고리즘

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b:
        parent[b]=a

    else:
        parent[a]=b


# 노드의 개수와 간선 입력받기
v, e = map(int,input().split())


parent=[0] * (v+1)

## 부모테이블을 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

cycle = False # 사이클 발생 여부


for i in range(e):
    a,b = map(int,input().split())
    # 사이클이 발생할경우 종료
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클발생')
else:
    print('사이클이발생하지아늠')


#####----------------------------------------------------------------------

############ 신장트리 
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 모든 노드가 다 연결되면서 사이클이 존재하지 않는다는 조건

#크루스칼 알고리즘(그리디 알고리즘)
#      동작과정
#  1. 간선데이터를 비용에 따라 오름 차순으로 정렬

#  2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인합니다.
#   1) 사이클이 발생하지 않는 경우 최소 신장트리에 포함
#   2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
#
#  3. 모든 간선에 대하여 2번의 과정을 반복합니다.

##          알고리즘

def union_find(parent,x):
    if parent[x] !=x:
        parent[x]=union_find(parent,parent[x])
    
    return parent[x]

def union_parent(parent,a,b):

    a= union_find(parent,a)
    b=union_find(parent,b)

    if b<a:
        parent[a]=b
    
    else:
        parent[b]=a

v,e = map(int,input().split()) #노드 번호, 간선입력
parent = [0]*(v+1) #1부터 시작하기 때문에 v+1

edges=[] #모든 간선을 담을 리스트

result = 0 # 최종비용을 담을 변수

for i in range(1,v+1): #부모테이블 초기화
    parent[i]=i

for _ in range(e):
    #a= 현재 노드 번호, b는 연결된 다음 노드, cost는 비용
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b)) # 비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인

for edge in edges:
    #cost 비용, a는 현재 노드, b는 연결된 다음 노드
    cost,a,b = edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)


## -----------------------------------------------------------------------

######### 위상정렬
# 사이클이 없는 방향크래프
# 큐를 이용하여 위상정렬 구현
# 1. 진입차수가 0인 모든 노드를 큐에넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복
#    1) 큐에 원소를 꺼내 해당 노드에 나가는 간선을 그래프에서 제거
#    2) 새롭게 진입차수가 0이된 노드를 큐에 넣는다

# 결과적으로 각노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과이다. 위상정렬은 여러개의 답이 존재할수잇음

from collections import deque

v, e = map(int,input().split())


# 모든 노드의 전입 차수를 0으로 처기화
indgree = [0] *(v+1)

graph= [[]for i in range(v+1)]

for i in range(e):
    # a= 현재노드. b= 연결된 다음 노드
    a ,b =map(int, input().split())
    graph[a].append(b)
    # 전입차수를 1증가
    indgree[b]+=1



# 위상 정렬 함수

def topology_sort():
    result = [] #수행 결과를 담는 리스트

    q= deque() 
    #처음시작할때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indgree[i]==0:
            q.append(i)

    while q: #큐가빌떄까지
        now = q.popleft()

        result.append(now)

        #해당 원소에 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indgree[i]-=1
            #새롭게 진입차수가 0이된느 노드를 큐에 삽입
            if indgree[i]==0:
                q.append(i)

    for i in result:
        print(i,end=' ')

topology_sort()
