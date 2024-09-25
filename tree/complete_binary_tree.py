# Problem : [완전 이진 트리] https://www.acmicpc.net/problem/9934
# Solver : 문지석
# Solved Date : 2024.09.10
# BigO: 2 ** n


from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    value: int
    left_child: object = None
    right_child: object = None


class Tree:
    def __init__(self, visited: list):
        self.head = None
        self.idx = 0 # visited 리스트의 인덱스로 사용할 것임
        self.visited = visited # 방문한 곳의 리스트를 받아옴

    def add_node(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            parent, child_pos = self.find_add_position()
            if child_pos == "L":
                parent.left_child = Node(value)
            elif child_pos == "R":
                parent.right_child = Node(value)

    def level_order(self):
        q = deque()
        q.append(self.head)
        value_list = []
        while len(q) != 0:
            cur_node = q.popleft()
            value_list.append(cur_node.value)

            if cur_node.left_child != None:
                q.append(cur_node.left_child)

            if cur_node.right_child != None:
                q.append(cur_node.right_child)

        return value_list

    def find_add_position(self):
        q = deque()
        q.append(self.head)
        while len(q) != 0:
            cur_node = q.popleft()

            if cur_node.left_child == None:
                return (cur_node, "L")
            elif cur_node.right_child == None:
                return (cur_node, "R")
            else:
                q.append(cur_node.left_child)
                q.append(cur_node.right_child)

    def inorder(self, is_start=True, node=None):
        '''
        inorder에서 print로 값을 출력하는 방식이 아니라
        입력된 순서대로 먼저 트리를 만든 후 inorder를 통해
        알맞은 순서대로 접근하여 값들을 수정하는 방식으로 바꿈.
        '''
        if is_start:
            node = self.head

        if node == None:
            return

        if node.left_child != None:
            self.inorder(is_start=False, node=node.left_child)

        node.value = self.visited[self.idx]
        self.idx += 1

        if node.right_child != None:
            self.inorder(is_start=False, node=node.right_child)


k = int(input())
visited_inorder = list(map(int, input().split()))
levelorder_buildings = Tree(visited_inorder)

for i in range(2**k - 1):
    levelorder_buildings.add_node(visited_inorder[i])

levelorder_buildings.inorder()

result_list = levelorder_buildings.level_order()

eol_list = [(2**i) - 1 for i in range(1, k)]
# end of line 할 위치 저장하는 리스트
tree_printed = ""
#출력될 트리 밑에 반복문에서 만듬

for i in range(2**k - 1):
    if i in eol_list:
        tree_printed += "\n"

    tree_printed += f"{result_list[i]} "

tree_printed = tree_printed.rstrip()
# 마지막 띄어쓰기 제거

print(tree_printed)
