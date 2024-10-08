# Problem : [1로 만들기] https://www.acmicpc.net/problem/1463
# Solver : 문지석
# Solved Date : 2024.10.05
# BigO: n


class one:
    def __init__(self, n):
        self.n = n
        self.count = {1: 0, 2: 1, 3: 1}

    def make_1(self):
        for i in range(4, self.n + 1):

            if i % 2 == 0 and i % 3 == 0:
                i_1 = i // 3
                i_2 = i // 2
                i_3 = i - 1
                smaller = min(self.count[i_1], self.count[i_2], self.count[i_3])
                self.count[i] = smaller + 1

            elif i % 2 == 0 and i % 3 != 0:
                i_1 = i // 2
                i_2 = i - 1
                smaller = min(self.count[i_1], self.count[i_2])
                self.count[i] = smaller + 1

            elif i % 2 != 0 and i % 3 == 0:
                i_1 = i // 3
                i_2 = i - 1
                smaller = min(self.count[i_1], self.count[i_2])
                self.count[i] = smaller + 1

            else:
                self.count[i] = self.count[i - 1] + 1

        return self.count[self.n]


x = int(input())
x2one = one(x)
print(x2one.make_1())
