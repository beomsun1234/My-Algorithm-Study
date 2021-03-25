# 다이나믹 프로그래밍
# 피보나치 수열


# 기본 피보나치 수

def fibo(n):
    if n ==1 or n== 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


#print(fibo(4))

##3----- dp 테이블 이용한 피보나치
#dp 테이블 초기화
d = [0]*100

# 첫번째, 두번째 피보나치수는  바텀업 방식으로 다이나믹 
# 바텀업
d[1]=1
d[2]=2
n=99
for i in range(3, n+1):
    d[i]= d[i-1]+ d[i-2]

#print(d[n])

# 탑다운 방식의 피보나치

d= [0]*100
def fibo_top_down(x):
    if x==1 or x==2:
        return 1

    if d[x]!=0: # 이미 계싼한적있는 문제라면 그대로 반환
        return d[x]

    d[x]= fibo(x-1)+fibo(x-2)
    return d[x]
#print(fibo_top_down(99))




## 다이나믹 프로그래밍고ㅓㅏ 분할 정복은 모두 최적 부분 구조를 가질 때 사용 할 수 있습니다

# 다이나믹과 분할 정복의 차이는 부분 문제의 중복이다.
# 다이나믹 에서는 가 부분 문제들이 서로 영향을 미치며 부분 문제가 중복됩니다
# 분할 정복 문제엣서는 동일한 부분 문제가 반복적으로 계산 되지 않습니다.




# 개미전사 문제

# 메뚜기 마을의 식랴ㅕㅇ창고를 공격, 메뚜기 마을에는 여러 개의 식량창고가 있고 식량창고는 일직선
# 각 식량창고에는 정해진 수익 식량을 저장하고 있으며 개미 전사는 식량 창고를 선택적으로 악탈 식량을 빼앗음

# 식량 창고 중에 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있음
# 예를 들어 식량창고  1 3 1 5 가 있으면 이때 두번째와 4번째 식량 창고를 선택했을때 8로 가장 많이 얻을수 있다
#식량창고 n개에 대한 정보가 주어졌을땨ㅐ 얻을수 있는 식량의 최대값을 구하라

#n= 식량창고의개수 k = 식량의 개수
# a = max(a[i-1], a[i-2]+k[i])
n = 4#int(input())
k = [1,2,1,5]#list(map(int, input().split()))
#print(k)
d=[0]*100
d[0]=1
d[1]=3

# 다이나믹 프로그래밍 보텀업
for i in range(2,len(k)):
    d[i]= max(d[i-1],d[i-2]+k[i])

# 계산된 결과 출력
#print(d[n-1])


## 1로 만들기 문제-------------------------------------------------
# 정수 x가 주어 졋을 때, 정수 x에 사욜할 수 있는 연산은 4가지
# 1. x가 5로 나누어 떨어디면, 5로 나눔
# 2. x가 3으로 나누어 떨어지면, 3으로 나눔
# 3. x가 2로 나 누어 떨어지면, 2로 나눔
# 4. x에서 1을 뺌

# 정수 x가 주어졌을때, 연산 4개를 적절히 사요ㅕㅇ해 값을 1로 만들고자 함
# 연산은 사용하는 횟수의 최솟값을 출력 0000000000000000
#  점화 식은 a = min(a[i-1],a[i/2], a[i/3],a[i/5]+1)

x =15#int(input())
result=0
d = [0] *30001 
for i in range(2, x+1):
    d[i]=d[i-1] + 1
    #print(i)
    if i % 2==0:
        d[i]=min(d[i],d[i//2]+1)
        print(d[i//2])
    if i %3==0:
        d[i]= min(d[i],d[i//3]+1)
    if i%5 ==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])
##----------------------------------------------------------


###### 효율적인 화페 구성문제--------------------------------
#
n,m = 5,15#map(int, input().split())

#dp 테이블 초기화
d=[10001]*(m+1)

d[0]=0
array=[]
for i in range(n):
    array.append(int(input()))

print(array)
for i in range(n): #i는 화페단위
    for j in range(array[i], m+1): #j는 각각의 화페금액
        if d[j-array[i]]!= 10001:
            print(j-array[i])
            d[j]=min(d[j],d[j-array[i]]+1)
            print('d[',j,']==',d[j])


if d[m]==10001:
    print(-1)
else:
    print(d[m])


## 금광 문제
# nxm의 금광이 있다. 1x1 크기의 칸으로 나누어져 있고, 각 칸은 특정한 크기의 금이있다

t =2#int(input())
n,m= 3,4#map(int,input().split())
gold= [1,3,3,2,2,1,4,1,0,6,4,7]#list(map(int,input().split()))
dp =[]
#1 3 3 2 2 1 4 1 0 6 4 7
index=0
for i in range(n):
    dp.append(gold[index:index+m])
    index+=m
print(dp)
for i in range(1,m):# 좌우
    for j in range(n): ##y 상하
        #왼쪽 위에서 오는 경우
        if j == 0: left_up = 0
        else: left_up = dp[j-1][i-1]

        #왼쪽 아래에서 오는 경우
        if  j==n-1: left_down=0
        else: left_down= dp[j+1][i-1]

        #왼쪽에서 오는 경우
        left = dp[j][i-1]

        dp[j][i] = dp[j][i]+max(left_up,left_down,left)

result = 0

# 가장 오른쪽 열에서 가장 큰값을 뽑으면
for i in range(n):
    result = max(result,dp[i][m-1])

print(result)





##병사 배치하기
# 각병사는 특정 값의 전투력 보유, 병사 배치시 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치 하고자함.
# 또한 배치과정에서 특정 위치에 있는 병사를 열외 시키는 방법을 이용함. 그러면서 병사수 최대가 되도록 하고싶음

n = int(input())
array = list(map(int,input().split()))

array.reverse()
dp = [1]*n
cnt=0
for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i]= max(dp[i],dp[j]+1)



print(n-max(dp))



