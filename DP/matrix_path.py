# Problem : [알고리즘 수업 - 행렬 경로 문제1] https://www.acmicpc.net/problem/24418
# Solver : 문지석
# Solved Date : 2025.01.07
# BigO :


class path:
    def __init__(self, n):
        self.mat_org = matrix
        self.mat_count = [[1] * n for _ in range(n)]
        self.n = n

    def recursive(self, x=1, y=1):
        for i in range(1, n):
            for j in range(1, n):
                self.mat_count[i][j] = (
                    self.mat_count[i - 1][j] + self.mat_count[i][j - 1]
                )

        return 2 * sum(self.mat_count[-1])

    def dynamic(self):
        return self.n**2


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    a = path(n)
    print(a.recursive(), a.dynamic())
