# Problem : [하노이 탑 이동 순서] https://www.acmicpc.net/problem/11729
# Solver : 문지석
# Solved Date : 2024.08.11
# BigO : 2 ** n


def moves(n):
    k = 1
    if n == 1:
        return k
    for _ in range(n - 1):
        k = 2 * k + 1
    return k


def track(org, n, dst):
    vst = 6 - (org + dst)
    if n > 2:
        return (
            track(org, n - 1, vst)
            + "\n"
            + track(org, 1, dst)
            + "\n"
            + track(vst, n - 1, dst)
        )

    if n == 2:
        str = f"{org} {vst}\n{org} {dst}\n{vst} {dst}"
        return str
    elif n == 1:
        str = f"{org} {dst}"
        return str


# track(1, n, 3) = track(1, n-1, 2) + track(1, 1, 3) + track(2, n-1, 3)
# 순서 역시 중요

n = int(input())
print(f"{moves(n)}")
print(f"{track(1, n, 3)}")
