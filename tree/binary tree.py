from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    value: int
    left_child: object = None
    right_child: object = None


class Tree:
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
        while len(q) != 0:
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
        while len(q) != 0:
            cur_node = q.popleft()

            if cur_node.left_child == None:
                return (cur_node, "L")
            elif cur_node.right_child == None:
                return (cur_node, "R")
            else:
                q.append(cur_node.left_child)
                q.append(cur_node.right_child)

    def find_delete_position(self, id):
        level_order_nodes = []

        q = deque()
        q.append(self.head)
        level_order_nodes.append((self.head, None, None))

        while len(q) != 0 or len(level_order_nodes) < id:
            cur_node = q.popleft()

            if cur_node.left_child != None:
                q.append(cur_node.left_child)
                level_order_nodes.append((cur_node.left_child, cur_node, "L"))
            if cur_node.right_child != None:
                q.append(cur_node.right_child)
                level_order_nodes.append((cur_node.right_child, cur_node, "R"))

        return level_order_nodes[id]

    def delete_node(self, id):
        d_node, d_node_parent, d_node_side = self.find_delete_position(id)
        if d_node.left_child != None and d_node.right_child != None:
            raise RuntimeError("There is childnode")
        del d_node
        if d_node_side == "R":
            d_node_parent.right_child = None
        if d_node_side == "L":
            d_node_parent.left_child = None

    def preorder(self, is_start=True, node=None):
        if is_start:
            node = self.head

        if node == None:
            return

        print(node.value)

        if node.left_child != None:
            self.preorder(is_start=False, node=node.left_child)
        if node.right_child != None:
            self.preorder(is_start=False, node=node.right_child)

    def inorder(self, is_start=True, node=None):
        if is_start:
            node = self.head

        if node == None:
            return

        if node.left_child != None:
            self.inorder(is_start=False, node=node.left_child)

        print(node.value)

        if node.right_child != None:
            self.inorder(is_start=False, node=node.right_child)

    def postorder(self, is_start=True, node=None):
        if is_start:
            node = self.head

        if node == None:
            return

        if node.left_child != None:
            self.postorder(is_start=False, node=node.left_child)

        if node.right_child != None:
            self.postorder(is_start=False, node=node.right_child)

        print(node.value)


if __name__ == "__main__":
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
    a.delete_node(4)
    print("---")
    a.level_order()
    print("add node")
    a.add_node(300)
    a.level_order()
    print("---")
    print("preorder")
    a.preorder(is_start=True)
    print("---")
    print("inorder")
    a.inorder(is_start=True)
    print("---")
    print("postorder")
    a.postorder(is_start=True)
