# Miller-Rabin 소수판별법 - O((logN)^3)
# Pollard-Rho 알고리즘 - O(N^(1/4))
# Eular-pi 함수

'''
1. 밀러 라빈 소수판별법
    확률적으로 소수를 빠르게 판별하는 알고리즘

    N이 아래 범위일 때에는 해당 수에 대해서만 확인해보면 된다는 것이 증명되어 있다.
    N < 1,373,653;      test = [2, 3]
    N < 9,080,191;      test = [31, 73]
    N < 4,759,123,141;  test = [2, 7, 61]
    N < 2,152,302,898,747       test = [2, 3, 5, 7, 11]
    N < 3,474,749,660,383       test = [2, 3, 5, 7, 11, 13]
    N < 341,550,071,728,321     test = [2, 3, 5, 7, 11, 13, 17]

2. 폴라드 로 소인수분해
    밀러-라빈 소수판별법을 이용해 소인수분해를 빠르게 하는 알고리즘

3. 오일러 피 함수
    서로소의 개수를 세는 함수
    폴라드 로 소인수분해와 함께 사용할 경우 빠르게 동작한다.
'''

from random import randrange
from math import gcd


# 밀러-라빈 소수판별법 서브 함수1
def modPow(base, exp, MOD):
    result = 1
    while exp:
        if exp & 1:
            result = (result*base) % MOD
        base = (base*base) % MOD
        exp >>= 1

    return result


# 밀러-라빈 소수판별법 서브 함수2
def MillerRabin(num, base):
    if num % base == 0:
        return False

    exp = num-1
    while True:
        temp = modPow(base, exp, num)
        if exp & 1:
            return True if temp != 1 and temp != num-1 else False
        elif temp == num-1:
            return False
        exp >>= 1


# 밀러-라빈 소수판별법
def isPrime(num):
    base = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}
    maxBase = base[-1]

    if num <= maxBase:
        if num in base:
            return True
        return False

    for i in base:
        if num == i:
            return True
        if MillerRabin(num, i) == True:
            return False
    if num <= maxBase:
        return False

    return True


# 폴라드-로 서브 함수1
def f(x, mod, c):
    return ((x*x)%mod + c) % mod


# 폴라드-로 서브 함수2
def cycle(num, factor):
    if num == 1:
        return
    if num % 2 == 0:
        factor.append(2)
        cycle(num//2, factor)
        return
    if isPrime(num) == True:
        factor.append(num)
        return

    while True:
        x = randrange(2, num)
        y = x
        c = randrange(1, num)
        d = 1
        while d == 1:
            x = f(x, num, c)
            y = f(f(y, num, c), num, c)
            d = gcd(abs(x-y), num)
        if d == num:
            continue
        break

    cycle(d, factor)
    cycle(num//d, factor)


# 폴라드 로 소인수분해 알고리즘
def PollardRho(num):
    factor = []
    cycle(num, factor)

    return sorted(factor)


# 오일러 피 함수
def EularPhi(num):
    primeF = list(set(PollardRho(num)))

    result = num
    for i in primeF:
        result -= result // i

    return result
