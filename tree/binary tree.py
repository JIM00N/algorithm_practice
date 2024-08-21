from dataclasses import dataclass
from collections import deque
@dataclass
class Node:
    value : int
    left_child : object = None
    right_child : object = None

class Tree():
    def __init__(self):
        self.head = None
    def set_test(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)

        node_1.left_child = node_2
        node_1.right_child = node_3
        node_2.left_child = node_4
        node_2.right_child = node_5
        self.head = node_1
        
    def add_node(self, value):
        if self.head==None:
            self.head = Node(value)
        else:
            parent, child_pos = self.find_add_position()
            if child_pos=="L":
                parent.left_child = Node(value)
            elif child_pos=="R":
                parent.right_child = Node(value)
        
    def level_order(self):
        q = deque()
        q.append(self.head)
        while len(q)!=0:
            cur_node = q.popleft()
            print(cur_node.value)
            if cur_node.left_child != None:
                q.append(cur_node.left_child)
                # print(f"line 1 {q}")
            if cur_node.right_child != None:
                q.append(cur_node.right_child)
                # print(f"line 2 {q}")
                
    def find_add_position(self):
        q = deque()
        q.append(self.head)
        while len(q)!=0:
            cur_node = q.popleft()

            if cur_node.left_child == None:
                return (cur_node, "L")
            elif cur_node.right_child == None:
                return (cur_node, "R")
            else:
                q.append(cur_node.left_child)
                q.append(cur_node.right_child)

            

if __name__=="__main__":
    a = Tree()
    # a.set_test()
    a.add_node(20)
    a.add_node(50)
    a.add_node(40)
    a.add_node(10)
    a.add_node(30)
    a.add_node(70)
    a.add_node(9)
    a.level_order()
