## 재귀함수 Recursuve Function 자기자신 호출

def recursive_func(i):
    if i==100:
        print('a')
        return
    print(i,"번째 재귀함수입니다.",i+1,"번째 재귀함수 호출합니다")
    recursive_func(i+1)
    print(i,"번째 재귀함수 종료합니다")

recursive_func(1)


##팩토리얼 구현 예제

def factorial_rec(n):
    if n <= 1:
        return 1
    return n*factorial_rec(n-1)

print(factorial_rec(5))

##최대 공약수 계산 (유클리드 호제법) 
# 두자연수 a,b 에 대하여 a를 b로나눈 나머지를 r이라고하면
# a와 bㅇ릐 최대공약수는 b와 r의 최대공약수오 ㅏ같다

a=192
b=162

def gcd(a,b):
    if a&b==0:
        return b
    else:
        return gcd(b,a%b)
        
print(gcd(192,162))