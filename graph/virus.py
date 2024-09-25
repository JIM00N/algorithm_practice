# Problem : [바이러스] https://www.acmicpc.net/problem/2606
# Solver : 문지석
# Solved Date : 2024.09.18
# BigO : n ** 2


import copy


class Graph:
    def __init__(self, couple_list, adjacency):
        self.couple = couple_list
        self.matrix = adjacency
        self.infected = 0
        self.counted = []

    def fill_info(self):
        for i in range(len(self.couple)):
            a_node = self.couple[i][0] - 1
            b_node = self.couple[i][1] - 1
            # 서로 연결이 된 노드들은 1로 바꿔
            self.matrix[a_node][b_node] = 1
            self.matrix[b_node][a_node] = 1
        return self.matrix

    def count_infected(self, id=0, is_start=False):
        # n ** 2
        if is_start == True:
            self.counted.append(0)
            # 미리 0번노드를 추가하여 
            # 0번 노드와 연결된 엣지를 중복으로 세는걸 방지
        for idx, val in enumerate(self.matrix[id]):
            if val == 1:
                self.matrix[id][idx] = 0
                self.matrix[idx][id] = 0
                # 세어줬으니 1 혹은 None과 혼동되지 않도록 0으로
                if idx not in self.counted:
                    # 이미 세어준 엣지가 아니라면(처음으로 세는 엣지라면)
                    self.infected += 1
                    self.counted.append(idx)
                    self.count_infected(idx)

computers = int(input())
couple = int(input())
couple_list = list()
# 입력 부분

for i in range(couple):
    couple_list.append(list(map(int, input().split())))
    
row = [None] * computers
# 연결이 안되는 간선은 None, 미리 None으로 초기화
adjacency_matrix = []
for i in range(computers):
    adjacency_matrix.append(copy.deepcopy(row))

virus = Graph(couple_list, adjacency_matrix)
infection_matrix = virus.fill_info()

virus.count_infected(0, is_start=True)
count = virus.infected

print(count)
