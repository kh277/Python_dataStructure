# Linear Sieve (오일러 체) - O(N)
# Factorize (소인수분해) - O(logN)

'''
구간 [1, N]에 존재하는 모든 소수를 구하는 선형 체. 
기존의 에라토스테네스의 체는 O(Nlog(logN))이 걸리지만,
합성수를 미리 제거하는 방식을 사용하면 O(N)으로 처리가 가능하다.

일반적인 나누기 알고리즘으로 소인수분해를 진행하는 경우 O(NlogN)이 걸리지만,
선형 체와 함께 사용하는 경우 선형 체 전처리 O(N) + 소인수분해 O(logN)으로 처리가 가능하다.
'''

from array import array


# N 이하의 소수 전부 반환
def LinearSieve(N):
    sieve = array('I', [0]) * (N+1)
    prime = array('I')

    for i in range(2, N+1):
        # 소수 추가
        if sieve[i] == 0:
            prime.append(i)
            sieve[i] = i

        # 합성수 제거
        for j in range(len(prime)):
            if i * prime[j] > N:
                break
            sieve[i * prime[j]] = prime[j]
            if i % prime[j] == 0:
                break

    return sieve, prime


# N을 소인수분해 한 결과 반환
def factorize(sieve, N):
    result = array('I')
    while N > 1:
        result.append(sieve[N])
        N = N // sieve[N]
    
    return result
