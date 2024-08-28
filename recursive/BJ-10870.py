# Ploblem : [피보나치 수 5] https://www.acmicpc.net/problem/10870
# Solver : 문지석
# Solved Date : 2024.08.11
# BigO: 2**n


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


n = int(input())
print(fibo(n))
