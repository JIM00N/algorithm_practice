# Problem : [트리] https://www.acmicpc.net/problem/1068
# Solver : 문지석
# Solved Date : 2024.09.18
# BigO: 2 ** n


from dataclasses import dataclass


@dataclass
class Node:
    number: int
    # child_list: list


class Tree:
    def __init__(self, parent_nodes: list):
        self.head = None  
        self.parents = parent_nodes
        # ex) 두번째 줄 입력이 4 4 4 4 -1 이라면
        # self.parents = [4, 4, 4, 4, -1] 각 요소의 인덱스는 해당 노드의 값, self.parent[index]는 부모 노드
        self.node_dict = dict()
        # { parent_node : [child_nodes], ....}
        for val in range(len(self.parents)):
            self.node_dict[val] = []
            # {0 : [], 1 : [], 2 : [], ...}
        self.leaf_count = 0

    def add_node(self, number):
        parent = self.parents[number]
        
        if self.parents[number] == -1:
            self.head = Node(number)
        else:
            a_node = Node(number)
            self.node_dict[parent].append(a_node)

    def delete_node(self, id):
        if self.parents[id] == -1:
            for child in list(self.node_dict.keys()):
                    del self.node_dict[child]

        elif self.parents[id] != -1:
            pos_in_parent = self.node_dict[self.parents[id]].index(Node(id))
            if self.node_dict[id] == []:
                del self.node_dict[self.parents[id]][pos_in_parent]
                del self.node_dict[id]
            else:
                for child in self.node_dict[id][::-1]:
                    self.delete_node(child.number)
                del self.node_dict[self.parents[id]][pos_in_parent]
                del self.node_dict[id]

    def how_many_leaves(self):
        child_list = list(self.node_dict.values())
        for child in child_list:
            if child == []:
                self.leaf_count += 1


nodes = int(input())
parent_node_list = list(map(int, input().split()))
d_node = int(input())

leaves = Tree(parent_node_list)

for num in range(len(parent_node_list)):
    leaves.add_node(num)

leaves.delete_node(d_node)
leaves.how_many_leaves()
print(leaves.leaf_count)
