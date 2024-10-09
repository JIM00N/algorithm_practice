# Problem : [2 * N 타일링2] https://www.acmicpc.net/problem/11727
# Solver : 문지석
# Solved Date : 2024.10.06
# BigO : n


def tiling2(n):
    seq = [1, 3]
    for i in range(3, n + 1):
        # a_k = a_k-1 + 3 * a_k-2 - a_k-2 = a_k-1 + 2 * a_k-2
        next = seq[-1] + 2 * seq[-2]
        next %= 10007
        seq.append(next)

    return seq[n - 1]


if __name__ == "__main__":
    n = int(input())
    print(tiling2(n))
