# 최소공배수구하기(수열 조합)


import math

math.lcm() #초소공배수
math.gcd()
t = 1#int(input())
array =[[]for i in range(t)]
for i in range(t):
    a,b = 13,14#map(int,input().split())
    array[i].append((a,b))


for i in range(t):
    x,y = array[i][0]
    print(math.lcm(x,y))
    print(math.gcd(x,y))


## 다이얼 문제(문자열)

#  전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 
#  숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 
#  다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
#  숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 
#  한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 
# 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
# 1은 알파벳 없음
# 2-> abc , 3= def, 4 ghi, 5= jkl, 6 mno,7 pqrs, 8 tuv
# 9 wxyz
# 단어의 길인ㄴ 2보다 크거나 같고 15보다 작거나 같다

a = 'UNUCIC'
result = 0
for i in a:
    if i == 'A' or i=='B' or i=='C':
        result+=3
    elif i == 'D' or i=='E' or i=='F':
        result+=4
    elif i == 'G' or i=='H' or i=='I':
        result +=5
    elif i== 'J' or i=='K' or i=='L':
        result+=6
    elif i == 'M' or i=='N' or i=='O':
        result +=7
    elif i =='P' or i=='Q' or i == 'R' or i == 'S':
        result+=8
    elif i == 'T' or i== 'U' or i =='V':
        result+=9
    print(i)

print(result)
        


##바이러스 문제(DFX, BFS):
#신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 
# 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
#예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 
# 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

n = 7#int(input()) #노드 개수
m = 6#int(input()) #간선
visited = [False]*(n+1)
graph = [[], [2, 5], [3], [], [7], [2, 6], [], []]#[[]for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

result =0 
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        #print(i)
        if not visited[i]:
            global result 
            result+=1
            dfs(graph,i,visited)
    return result

    
print(dfs(graph,1,visited))


## 단지 번호 붙이기
#정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

n = int(input()) # 정사각형

graph = [list(map(int,input()))for i in range(n)]
total=0
dx = [-1,1,0,0] # 좌우
dy = [0,0,-1,1] # 상하
cnt=0
a=[]
def dfs1(i,j):
    for way in range(4):
        ii, jj = dx[way]+i, dy[way]+j 
        if ii < 0 or ii>=n or jj <0 or jj>=n:
            continue
        if graph[ii][jj]==1:
            graph[ii][jj]=0
            dfs1(ii,jj)
            global cnt
            cnt+=1
    return cnt
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            a.append(dfs1(i,j))
            cnt=0 
            total +=1
            

print(total)
a.sort()

for i in range(len(a)):
    if a[i]==0:
        a[i]=1
    print(a[i])

###------------------------------------------------------------------



## 유기농 배추 문제 (dfs, bfs)

#차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
#농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 
# 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 
# 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어
# ,그 배추들 역시 해충으로부터 보호받을 수 있다.
# (한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

#한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
#(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)

array=[]
import sys 
sys.setrecursionlimit(10**6)  #재귀 깊이 설정
t = int(input()) #테스트
#  케이스 개수
cnt=0
#가로 = m 세로는 =n , 배추의 개수=k
while (cnt!=t):
    cnt+=1
    m,n,k = map(int,input().split())
    graph=[[0]*m for i in range(n)]

#열x행 
    for i in range(k):
        x,y = map(int, input().split())
        graph[y][x] =1


    dx = [-1,1,0,0] # 좌우
    dy = [0,0,-1,1] # 상하


    def dfs2(i,j):
        for way in range(4):
            ii, jj = dx[way]+i, dy[way]+j
            if ii<0 or ii>=n or jj<0 or jj>=m:
                continue
            if graph[ii][jj]==1:
                graph[ii][jj]=0
                dfs2(ii,jj)
        return False
    result =0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                result+=1
                dfs2(i,j)

    array.append(result)

for i in array:
    print(i)



####------------------------------------------