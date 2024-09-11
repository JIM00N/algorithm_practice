# Problem : [트리] https://www.acmicpc.net/problem/1068
# Solver : 문지석
# Solved Date : 2024.09.10
# BigO: 2 ** n


from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    number: int
    child_list: list


class Tree:
    def __init__(self, parent_nodes: list):
        self.head = None  # ex) 두번째 줄 입력이 4 4 4 4 -1 이라면
        self.parents = parent_nodes
        # self.parents = [4, 4, 4, 4, -1] 각 요소의 인덱스는 해당 노드의 값, self.parent[index]는 부모 노드의 인덱스
        self.node_list = [None] * 50
        # add_node를 거치면 / self.node_list = [Node(0,[]), Node(1,[]), Node(2,[]), Node(3,[]), Node(4,[]), none ...]
        self.leaf_count = 0

    def add_node(self, number, parent_node):
        if parent_node == -1:
            self.head = Node(number)
            self.node_list[number] = self.head

        else:
            a_node = Node(number)
            self.node_list[number] = a_node

    def link_nodes(self):
        for idx, parent in enumerate(self.parents):
            if parent == -1:
                continue
            self.node_list[parent].child_list(self.node_list[idx])

    def delete_node(self, node=None, id=None):
        if id == None and node == None:
            return

        if id != None and node == None:
            d_node = self.node_list[id]

            for i in d_node.child_list:
                self.delete_node(i, None)

            d_node = None

        elif id == None and node != None:
            for i in node.child_list:
                self.delete_node(i, None)

            node = None

    def how_many_leaves(self, is_start=True, node=None):
        if is_start:
            node = self.head
            if self.head == None:
                return 0

        if node == None:
            return


nodes = int(input())
parent_node_list = list(map(int, input().split()))
remove_node = int(input())

leaves = Tree(parent_node_list)

for num, parent_node in enumerate(parent_node_list):
    # 노드의 번호를 num, 부모 노드의 번호를 parent_node로 분리해서 받는다.
    leaves.add_node(num, parent_node)

leaves.delete_node(None, remove_node)

leaves.how_many_leaves()

print(leaves.leaf_count)
