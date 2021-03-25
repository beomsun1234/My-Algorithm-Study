##선택정렬


array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index], array[i] # 스와프

print(array)


# 삽입정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]< array[j-1]: #자신이랑 비교한후 크면 바꿈
            array[j],array[j-1]=array[j-1], array[j] #스왑 #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else:
            break


print(array)


#퀵정렬

array1 = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:
         # 원소가 한개인경우 종료
         return

    pivot = start

    left = start +1
    right = end

    while (left<=right):
        while (left<=end and array1[left]<=array1[pivot]):
            left+=1
        while (right > start and array1[right] >= array1[pivot] ):
            right-=1
        if left > right: ## 엇갈렸다면 작은 데이터와 피벅을 교체
            array1[right], array1[pivot] = array1[pivot], array1[right]

        else:
            array1[left], array1[right]= array1[right], array1[left]

    quick_sort(array1,start,right-1)
    quick_sort(array1,right+1,end)

quick_sort(array1,0,len(array1)-1)
print(array1)


### 개수 정렬

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

print(array)
cnt = [0]*(len(array))
print(cnt)

for i in range(len(array)):
    cnt[array[i]]+=1
    print(cnt)

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i,end=' ')

print("\n",'--------------------','\n')
##--------------------------------

##두 배열 원소 교체
# a와 b를 k 번 바꿔치기 해서 a리스트의 합이 가장 큰값 만들기

n,k = 5,3#map(int,input().split())
a = [1,2,5,4,3]#list(map(int,input().split()))
b = [5,5,6,6,5]#list(map(int,input().split()))
a.sort() # a의 가장 작은 값과  b에서 가장 큰값을 찾아서 바꾸기위해 a는 오름차순 정렬
b.sort(reverse=True) #b는 내림차순 정렬
print(a,b) 

for i in range(k):
    if a[i]<b[i]: #a와b 비교후 b가 더 크면 교체
        a[i],b[i]= b[i],a[i]
    else:
        break

print(sum(a))

######## 