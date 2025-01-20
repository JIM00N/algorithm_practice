# 2025/01/08
# Kruskal
class MST:
    def __init__(self, num_nodes, edges: list):
        self.num = num_nodes
        edges.sort()
        self.edges = edges
        self.parent = {chr(97+i): [chr(97+i), 0] for i in range(self.num)}
        self.sum = 0
        

    def union(self):
        for edge in self.edges:
            weight, x, y = edge[0], edge[1], edge[2]
            mode = self.parent[x][-1] + self.parent[y][-1]
            if mode == 0:
                self.parent[x][-1] = 1
                self.parent[y][-1] = 1
                self.parent[y][0] = x
                self.sum += weight

            elif self.parent[x][-1] == 1 and mode == 1:
                self.parent[y][-1] = 1
                self.parent[y][0] = x
                self.sum += weight

            elif self.parent[y][-1] == 1 and mode == 1:
                self.parent[x][-1] = 1
                self.parent[x][0] = y
                self.sum += weight
            # if self.parent[x][-1] != 1 or self.parent[y][-1] != 1:
            #     self.parent[x][-1] = 1
            #     self.parent[y][-1] = 1
            #     self.sum += weight
            #     if self.parent[x][-1] == 1 or mode == 0:
            #         self.parent[y][0] = x
            #     else:
            #         self.parent[x][0] = y

            else:
                x_root, y_root = self.find(x), self.find(y)
                
                if x_root < y_root:
                    self.change_parent(y, y_root)
                    self.parent[y][0] = x
                    self.sum += weight
                elif x_root > y_root:
                    self.change_parent(x, x_root)
                    self.parent[x][0] = y
                    self.sum += weight
                

    def find(self, node):
        if self.parent[node][0] == node:
            return node
        else:
            return self.find(self.parent[node][0])
        
    def change_parent(self, node, root_node, prev_node=None):
        if node == root_node:
            self.parent[node][0] = prev_node
        else:
            prev_node = node
            node = self.parent[node][0]
            self.change_parent(node, root_node, prev_node)
            self.parent[node][0] = prev_node


if __name__ == "__main__":
    num_nodes, num_edges = tuple(map(int, input().split()))
    edge_list = []
    for _ in range(num_edges):
        org, dst, weight = tuple(input().split())
        if dst < org:
            org, dst = dst, org
        edge_list.append([int(weight), org, dst])

    mst = MST(num_nodes, edge_list)
    print(edge_list)
    mst.union()
    print(mst.sum)
    print(mst.parent)
