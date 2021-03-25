#이진 탐색
# 재귀 함수 구현
from bisect import bisect_left,bisect_right
def binary_search_recu(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search_recu(array,target,start,mid-1)
    
    else:
        return binary_search_recu(array,target,mid+1,end)
    

n, target = 10, 7 
array = [1,3,5,7,9,11,13,15,17,19]
print('라이브러리 사용하면=',bisect_left(array,7)+1)
array.sort()

result = binary_search_recu(array,target,0,n-1)

if result ==None:
    print('XXXXX')
else:
    print('재귀함수 사용해서=',result+1)
print(array)

### 반복문 구현

def binary_search_loop(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid

        elif array[mid] > target:
            end = mid -1

        else:
            start = mid+1
    return None



n, target = 10, 7 
array = [1,3,5,7,9,11,13,15,17,19]
array.sort()
result = binary_search_loop(array,target,0,n-1)
if result ==None:
    print('XXXXX')
else:
    print(result+1)
print(array)


### 파이썬 이진 탐색 라이브러리

#bisect_left(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 사입할 가장 왼쪽 인덱스를 반환
#bisect_right(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left,bisect_right

a=[1,2,4,4,8]
x=4
print(bisect_left(a,x))
print(bisect_right (a,x))

## 값이 특정 범위에 속하는 데이터 개수구하기

from bisect import bisect_left,bisect_right

def coun_by_range(a,left_val,right_val):
    right_val = bisect_right(a,right_val)
    left_val = bisect_left(a,left_val)
    return right_val - left_val

a=[1,2,3,3,3,3,4,4,8,9]

print(coun_by_range(a,4,8))


print(coun_by_range(a,-1,3)) ## 값이 [-1,3] 범위에 있는 데이터 개수 출력


### 파라메트릭 서치 = 최적화 결정 문제(예, 혹은 아니오)로 바꾸어 해결하는 기법


# 떡볶이 떡 만들기 (bisect_right)
# 떡길이 일정하지 아늠 대신 한봉지안에 들어가는 떡의 총길이는 절단기로 잘라서 맞춰줌
# 절단기 높이르 지정하면 한번에 절단, 높이가 h보다 긴 떡은 h의 위 부분이 잘림 낮은 떡은 안잘림

# 19 14 10 17 이 절단기 15로 지정하면 15 14 10 15 가 되며 떡의 길이는 4 0 0 2 손님은 6 의 길이를 가져감
from bisect import bisect_left,bisect_right



#bisect_right(h,m)

#print(bisect_right(h,m))
#def test(array,target,start, end):
    # if start>end:
        # return None
    # mid = (start+end)//2
# 
    # if array[mid]<=target:
        # return 0
    # elif array[mid]>target:
        # a=array[mid]-target
        # return test(array,target,mid+1,end)
    # 
    # if 
# n,m = map(int,input().split())
# h = list(map(int,input().split()))
# h.sort()
# print(h)
# result = test(h,m,0,n-1)


##------------------------
# 떡볶이 떡 만들기 (bisect_right)
# 떡길이 일정하지 아늠 대신 한봉지안에 들어가는 떡의 총길이는 절단기로 잘라서 맞춰줌
# 절단기 높이르 지정하면 한번에 절단, 높이가 h보다 긴 떡은 h의 위 부분이 잘림 낮은 떡은 안잘림

# 19 14 10 17 이 절단기 15로 지정하면 15 14 10 15 가 되며 떡의 길이는 4 0 0 2 손님은 6 의 길이를 가져감
n,m = 4,6#list(map(int,input().split(' ')))
h = [19,15,10,17] #list(map(int,input().split()))

start = 0
end = max(h) #가지고 있는 떡의 길이중 가장 큰 값
print(end)

ccc = 0
#이진탐색 수행
total = 0
while (start<=end):
    total = 0
    mid=(start+end)//2 ##
    #print(mid)
    for i in h:
        if i> mid: #현재 떡의 길이가 높이보다 클때만 떡계산
            total += i-mid
            print('i,mid,total',i,mid,total)
    if total <m:
        end= mid-1
    else:
        ccc = mid
        print(mid)
        start=mid +1

print(ccc)



#4 6
#19 15 10 17


###############
#정렬된 배열에서 특정 수의 개수 구하기
# 오름차순의로 정렬된 수열 X=[1,1,2,2,2,3] ㅣ있을때 X=2라면 현재수열에서 값이 2인 원소가 4개이므로 4를 출력
# n개의 원소를 포함하고 있는 수열 x= 현재 수열의 값
from bisect import bis
n,x = map(int,input().split())

num = list(map(int, input().split()))

print(num)
