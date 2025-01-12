# 2025/01/08
# Kruskal
class MST:
    def __init__(self, num_nodes, edges: list):
        self.num = num_nodes
        edges.sort()
        self.edges = edges
        self.group = {chr(97 + i): chr(97 + i) for i in range(self.num)}
        self.sum = 0

    def link(self):
        mode = 0
        # 0 -> 다른 영역 = 연결 후 영역표시, 1 -> 같은 영역 = pass
        for edge in self.edges:
            org_dst = sorted([edge[1], edge[2]])
            org, dst = org_dst[0], org_dst[1]
            if org == self.group[org] and dst == self.group[dst]:
                mode = 0

            elif org == self.group[org]:
                if self.group[dst] == self.group[org]:
                    mode = 1
                else:
                    mode = 0
                    if self.group[dst] < org:
                        org, dst = dst, org

            elif dst == self.group[dst]:
                mode = 0

            else:
                if self.group[dst] == self.group[org]:
                    mode = 1
                else:
                    mode = 0
                    if self.group[dst] < org:
                        org, dst = dst, org

            self.compare(mode, org, dst, edge[0])

    def make_group(self, g_alpha, del_alpha):
        for i in range(self.num):
            if self.group[chr(97 + i)] == del_alpha:
                self.group[chr(97 + i)] = g_alpha

    def compare(self, mode, org, dst, weight):
        if mode == 0:
            self.make_group(self.group[org], self.group[dst])
            self.sum += weight
        if mode == 1:
            pass


if __name__ == "__main__":
    num_nodes, num_edges = tuple(map(int, input().split()))
    edge_list = []
    for _ in range(num_edges):
        org, dst, weight = tuple(input().split())
        edge_list.append((int(weight), org, dst))

    mst = MST(num_nodes, edge_list)
    mst.link()
    print(mst.group)
    # print(mst.edges)
    print(mst.sum)
