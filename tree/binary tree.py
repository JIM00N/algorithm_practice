from dataclasses import dataclass
@dataclass
class Node:
    value : int
    left_child : object = None
    right_child : object = None

# if __name__=="__main__":
#     node = Node(10)
#     print(node.value)
#     print(node.left_child)
#     print(node.right_child)
#     node1 = Node(20)
#     print(node1.value)
#     node.left_child = node1
#     print(node.left_child.value)
#     node1.value = 40
#     print(node.left_child.value)
#     print(node1.value)