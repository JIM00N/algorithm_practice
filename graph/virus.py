# Problem : [바이러스] https://www.acmicpc.net/problem/2606
# Solver : 문지석
# Solved Date : 2024.09.10
# BigO : 


import copy
from dataclasses import dataclass

class Node:
    number: int
    edge: list

class Graph:
    def __init__(self, couple_list, adjacency):
        self.couple = couple_list
        self.matrix = adjacency
    
    def fill_info(self):
        for i in range(len(self.couple)):
            a_node = self.couple[i][0] - 1
            b_node = self.couple[i][1] - 1

            self.matrix[a_node][b_node] = 1
            self.matrix[b_node][a_node] = 1

        return self.matrix

computers = int(input())
couple = int(input())
couple_list = list()

for i in range(couple):
    couple_list.append(list(map(int, input().split())))

row = [None] * computers
adjacency_matrix = []
for i in range(computers):
    adjacency_matrix.append(copy.deepcopy(row))

infection = Graph(couple_list, adjacency_matrix)

infection_matrix = infection.fill_info()

count = 0

# matrix는 완성했음 tree 알고리즘 이용해서 마지막 해결할 것
