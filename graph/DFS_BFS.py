# Problem : [DFS와 BFS]] https://www.acmicpc.net/problem/1260
# Solver : 문지석
# Solved Date : 2024.09.28
# BigO: n ** 2



import copy


class DFS:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.node_num = len(adjacency_matrix)
        self.visit = [False] * self.node_num
        self.result = []

    def dfs(self, cur_id):
        self.visit[cur_id] = True
        self.result.append(cur_id)
        for target_id in range(self.node_num):
            if (
                self.matrix[cur_id][target_id] == True
                and self.visit[target_id] == False
            ):
                self.dfs(target_id)

    def get_result(self):
        return map(lambda x: x + 1, self.result)


class BFS:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.node_num = len(self.matrix)
        self.visit = [False] * self.node_num

        self.result = []

    def bfs(self, cur_id):
        queue = [cur_id]
        self.visit[cur_id] = True
        
        while len(queue) != 0:
            cur_node = queue.pop(0)
            self.result.append(cur_node)
            for next_node, t_f in enumerate(self.matrix[cur_node]):
                if t_f == True and self.visit[next_node] == False:
                    self.visit[next_node] = True
                    queue.append(next_node)

    def get_result(self):
        return map(lambda x: x + 1, self.result)


def init_mat(n):
    row = [False] * n
    matrix = []
    for i in range(n):
        matrix.append(copy.deepcopy(row))
    return matrix


if __name__ == "__main__":
    num_nodes, num_edge, start_node = tuple(map(int, input().split()))
    start_node = start_node - 1
    adjacency_matrix_dfs = init_mat(num_nodes)
    adjacency_matrix_bfs = init_mat(num_nodes)

    for _ in range(num_edge):
        node_1, node_2 = tuple(map(int, input().split()))
        node_1 = node_1 - 1
        node_2 = node_2 - 1

        adjacency_matrix_bfs[node_1][node_2] = True
        adjacency_matrix_bfs[node_2][node_1] = True

        adjacency_matrix_dfs[node_1][node_2] = True
        adjacency_matrix_dfs[node_2][node_1] = True

    # my_dfs = DFS(adjacency_matrix_dfs)
    # my_dfs.dfs(start_node)
    # print(" ".join(map(str, my_dfs.get_result())))

    my_bfs = BFS(adjacency_matrix_bfs)
    my_bfs.bfs(start_node)
    print(" ".join(map(str, my_bfs.get_result())))
