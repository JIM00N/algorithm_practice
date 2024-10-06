# Problem : [2 * N 타일링2] https://www.acmicpc.net/problem/11727
# Solver : 문지석
# Solved Date : 2024.10.06
# BigO : n


def tiling2(n):
    seq = [1, 3]
    for i in range(3, n + 1):
        if i % 2 == 0:
            next = 4 * seq[i - 3] - 1
        else:
            next = 2 * seq[i - 2] - 1

        next %= 10007
        seq.append(next)

    return seq[n - 1]


if __name__ == "__main__":
    n = int(input())
    print(tiling2(n))
