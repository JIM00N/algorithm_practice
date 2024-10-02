# Ploblem : [피보나치 수 7] https://www.acmicpc.net/problem/15624
# Solver : 문지석
# Solved Date : 2024.10.2
# BigO: n


def fibo7(n):
    first = 0
    second = 1
    last = first + second
    for _ in range(n - 2):
        first = second
        second = last
        last = (first + second) % 1000000007
    
    if n == 0:
        return 0

    return last

n = int(input())

print(fibo7(n))
