# Ploblem : [쿼드트리] https://www.acmicpc.net/problem/1992
# Solver : 문지석
# Solved Date : 2024.09.03
# BigO : n ** 2


def quad_tree(n, video, row=0, col=0):
    count_1 = 0
    count_0 = 0
    half_n = int(n / 2)
    for i in range(row, row + n):
        for j in range(col, col + n):
            if video[i][j] == "1":
                count_1 += 1
            else:
                count_0 += 1

    if count_1 == n**2:
        return "1"
    elif count_0 == n**2:
        return "0"
    else:
        left_top = quad_tree(half_n, video, row, col)
        right_top = quad_tree(half_n, video, row, col + half_n)
        left_bottom = quad_tree(half_n, video, row + half_n, col)
        right_bottom = quad_tree(half_n, video, row + half_n, col + half_n)
        return f"({left_top + right_top + left_bottom + right_bottom})"


n = int(input())

video = []
for _ in range(n):
    video.append(input())

compressed = quad_tree(n, video)
print(compressed)
