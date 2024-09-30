# Problem : [단지번호붙이기] https://www.acmicpc.net/problem/2667
# Solver : 문지석
# Solved Date : 2024.09.30
# BigO : n ** 2
import copy


class address:
    def __init__(self, town, visit):
        self.n = len(town)
        self.matrix = town
        self.visit = visit
        self.num_towns = 0
        self.kind_towns = []

    def count(self):
        for i in range(n):
            for j in range(n):
                if int(self.matrix[i][j]) == 1 and self.visit[i][j] == False:
                    self.num_towns = 1
                    self.visit[i][j] = True
                    self.move([i, j])
                    self.kind_towns.append(self.num_towns)
                    self.num_towns = 0

    def move(self, pos):
        col, row = pos[0], pos[1]
        up = [col + 1, row]
        down = [col - 1, row]
        right = [col, row + 1]
        left = [col, row - 1]

        if up[0] < self.n and self.visit[up[0]][up[1]] == False:
            if int(self.matrix[up[0]][up[1]]) == 1:
                self.num_towns += 1
                self.visit[up[0]][up[1]] = True
                self.move([up[0], up[1]])
        if down[0] >= 0 and self.visit[down[0]][down[1]] == False:
            if int(self.matrix[down[0]][down[1]]) == 1:
                self.num_towns += 1
                self.visit[down[0]][down[1]] = True
                self.move([down[0], down[1]])
        if right[1] < self.n and self.visit[right[0]][right[1]] == False:
            if int(self.matrix[right[0]][right[1]]) == 1:
                self.num_towns += 1
                self.visit[right[0]][right[1]] = True
                self.move([right[0], right[1]])
        if left[1] >= 0 and self.visit[left[0]][left[1]] == False:
            if int(self.matrix[left[0]][left[1]]) == 1:
                self.num_towns += 1
                self.visit[left[0]][left[1]] = True
                self.move([left[0], left[1]])

    def get(self):
        return self.kind_towns


n = int(input())

town = []

for i in range(n):
    row_input = input()
    town.append(row_input)

row = [False] * n
visit_or_not_matrix = []
for i in range(n):
    visit_or_not_matrix.append(copy.deepcopy(row))

post = address(town, visit_or_not_matrix)
post.count()
result_list = post.get()
result_list = sorted(result_list)  # n * log(n)

for i in range(len(result_list)):
    if i == 0:
        print(len(result_list))

    print(result_list[i])
