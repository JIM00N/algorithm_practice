# Problem : [전쟁-전투] https://www.acmicpc.net/problem/1303
# Solver : 문지석
# Solved Date : 2024.09.28
# BigO : n ** 2
import copy


class war:
    def __init__(self, soldiers, visit):
        self.matrix = soldiers
        self.visit = visit
        self.len_col = len(soldiers)
        self.len_row = len(soldiers[0])
        self.power = {"W": 0, "B": 0}
        self.my_team = 1

    def count(self):
        for i in range(self.len_col):
            for j in range(self.len_row):
                if self.visit[i][j] == True:
                    continue

                else:
                    self.visit[i][j] = True
                    self.move([i, j], self.matrix[i][j])
                    self.power[self.matrix[i][j]] += self.my_team**2
                    self.my_team = 1
        print(f"{self.power['W']} {self.power['B']}")

    def move(self, pos, team):
        col, row = pos[0], pos[1]
        up = [col + 1, row]
        down = [col - 1, row]
        right = [col, row + 1]
        left = [col, row - 1]

        # 위 아래 오른쪽 왼쪽으로 움직이고 그 자리에서 재귀
        if up[0] < self.len_col and self.visit[up[0]][up[1]] == False:
            if self.matrix[up[0]][up[1]] == team:
                self.my_team += 1
                self.visit[up[0]][up[1]] = True
                self.move([up[0], up[1]], team)

        if down[0] >= 0 and self.visit[down[0]][down[1]] == False:
            if self.matrix[down[0]][down[1]] == team:
                self.my_team += 1
                self.visit[down[0]][down[1]] = True
                self.move([down[0], down[1]], team)

        if right[1] < self.len_row and self.visit[right[0]][right[1]] == False:
            if self.matrix[right[0]][right[1]] == team:
                self.my_team += 1
                self.visit[right[0]][right[1]] = True
                self.move([right[0], right[1]], team)

        if left[1] >= 0 and self.visit[left[0]][left[1]] == False:
            if self.matrix[left[0]][left[1]] == team:
                self.my_team += 1
                self.visit[left[0]][left[1]] = True
                self.move([left[0], left[1]], team)

if __name__ == "__main__":
    len_row, len_col = tuple(map(int, input().split()))
    battle_ground = []

    for i in range(len_col):
        row_input = input()
        battle_ground.append(row_input)

    # 지나간데 안지나간데 매트릭스
    row = [False] * len_row
    visit_or_not_matrix = []
    for i in range(len_col):
        visit_or_not_matrix.append(copy.deepcopy(row))

    power = war(battle_ground, visit_or_not_matrix)
    power.count()
