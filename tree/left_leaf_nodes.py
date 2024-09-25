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
        for val in range(len(self.parents)):
            self.node_dict[val] = []
            # {parent_node number : [child_nodes], ....}
            # {0 : [], 1 : [], 2 : [], ...}
        self.leaf_count = 0

    def add_node(self, number):
        parent = self.parents[number]
        # 루트 노드인지 아닌지 확인
        if self.parents[number] == -1:
            # 루트 노드라면
            self.head = Node(number)
        else:
            # 루트 노드가 아니라면
            a_node = Node(number)
            self.node_dict[parent].append(a_node)
            # 딕셔너리의 부모노드에 자식으로 추가

    def delete_node(self, id):
        if self.parents[id] == -1:
            # 루트 노드를 지운다면 딕셔너리 모두 삭제
            for parent in list(self.node_dict.keys()):
                    del self.node_dict[parent]

        elif self.parents[id] != -1:
            # 루트 노드 아닌 노드를 지운다면
            pos_in_parent = self.node_dict[self.parents[id]].index(Node(id))
            # 딕셔너리의 부모노드 자식 리스트에서 자신의 위치를 찾고
            if self.node_dict[id] == []:
                # 자식이 없다면
                del self.node_dict[self.parents[id]][pos_in_parent]
                # 부모노드에서 자신을 삭제
                del self.node_dict[id]
                # 딕셔너리에서 자신을 삭제
            else:
                # 자식이 있다면
                for child in self.node_dict[id][::-1]:
                    # 낮은 번호의 자식 노드들을 먼저 지우면 
                    # 높은 노드들의 인덱스가 바뀌기에 높은 번호의 자식 노드들부터 삭제
                    self.delete_node(child.number) # 재귀

                del self.node_dict[self.parents[id]][pos_in_parent]
                # 부모노드에서 자신을 삭제
                del self.node_dict[id]
                # 딕셔너리에서 자신을 삭제

    def how_many_leaves(self):
        # 딕셔너리에서 value에 빈리스트의 개수가 리프노드의 개순
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
