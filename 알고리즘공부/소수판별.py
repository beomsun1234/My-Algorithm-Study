# 기본 소수 판별 알고리즘

def is_prime_number(x):
    for i in range(2, x):
        if x % i==0: #나누어 떨어지면
            return False
    return True

if is_prime_number(6):
    print("소수입니다")
else:
    print('소수아님')

## 약수의 성질을 이용한제곱근을 사용하느 개선된 소수 판별

import math

# 소수 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근 까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i ==0:
            return False #소수가 아님
    return True #소수임


print(is_prime_number(4))
print(is_prime_number(7))


#시간복잡도는 o(n의 2분에 1승)
####------------------------------------------------

## 다수의 소수 판별
# 하나의 수에 대해서 소수인지 아닌지 판별하는 방법을 알아보자
# 하지만 특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할 때는 어떻게 할까?
# - 에라토스테네스의 체 알고리즘을 사용

# 다수의 자연수에 대하여 소수 여부를 판별할 때 사용하는 대포적 알고리즘
# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

## 에라토스테네스의 체 알고리즘의 동장
# 1. 2부터 N까지의 모든 자연수를 나열한다.
# 2. 남은 수중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다

import math

n= 1000 # 2부터 1000 까지의 모든 수에 대하여 소수 판별


#처음엔 모든 수가 소수 인것으로 초기화
array = [True for i in range(n+1)]

