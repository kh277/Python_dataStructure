# 기본 수학 함수


# 최대공약수
def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def LCM(a, b):
    return a * b // GCD(a, b)


# 소수 판정 - O(sqrt(N))
def isPrime(N):
    if N <= 1:
        return False
    elif N <= 3:
        return True
    elif N % 2 == 0 or N % 3 == 0:
        return False

    for i in range(5, int(N**0.5)+1, 6):
        if N % i == 0 or N % (i + 2) == 0:
            return False

    return True