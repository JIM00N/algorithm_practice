# Problem : [2 * N 타일링] https://www.acmicpc.net/problem/11726
# Solver : 문지석
# Solved Date : 2024.10.02
# BigO : n


def tiling(n):
    seq = [1, 2]
    for _ in range(1, n):
        next = (seq[-1] + seq[-2]) % 10007
        seq.append(next)
    
    return seq[n-1]

n = int(input())
print(tiling(n))
