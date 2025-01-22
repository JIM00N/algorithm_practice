# Huffman coding
import heapq
from dataclasses import dataclass


@dataclass
class Node:
    frequency: int
    chr: str = None
    left_child: list = None
    right_child: list = None
    id: str = ""


class huffman:
    def __init__(self, char_num, data):
        self.data = data
        self.result = char_num

    def popNpush(self):
        while len(self.data) != 1:
            smaller = heapq.heappop(self.data)
            larger = heapq.heappop(self.data)

            sum = smaller[0] + larger[0]  # 가중치 더하기
            new_node = Node(
                sum, "~", larger, smaller
            )  # 물결 표시가 알파벳보다 아스키 코드가 뒤임

            heapq.heappush(self.data, [sum, "~", new_node])

    def tracking_tree(self):
        root_node_data = heapq.heappop(self.data)
        root_node = root_node_data[2]
        if root_node.right_child != None:
            self.go_right(root_node.right_child[2], root_node.id)
        if root_node.left_child != None:
            self.go_left(root_node.left_child[2], root_node.id)

    def go_right(self, r_child, cur_id):
        r_child.id = cur_id + "1"

        if r_child.right_child != None:
            self.go_right(r_child.right_child[2], r_child.id)
        if r_child.left_child != None:
            self.go_left(r_child.left_child[2], r_child.id)

        if r_child.chr != "~":
            self.result[r_child.chr][1] = r_child.id

    def go_left(self, l_child, cur_id):
        l_child.id = cur_id + "0"

        if l_child.right_child != None:
            self.go_right(l_child.right_child[2], l_child.id)
        if l_child.left_child != None:
            self.go_left(l_child.left_child[2], l_child.id)

        if l_child.chr != "~":
            self.result[l_child.chr][1] = l_child.id


if __name__ == "__main__":
    text = "AAAAAAABBCCCDEEEEFFFFFFG"
    char_num = {}
    for char in text:
        try:
            char_num[char][0] += 1
        except:
            char_num[char] = [1, ""]

    dsc_order_char_num = []
    for key, value in char_num.items():
        value = value[0]
        heapq.heappush(dsc_order_char_num, [value, key, Node(value, key)])

    huffman_code = huffman(char_num, dsc_order_char_num)
    huffman_code.popNpush()
    huffman_code.tracking_tree()

    print(huffman_code.result)

    compressed_bit = ""
    for alpha in text:
        compressed_bit += char_num[alpha][1]

    print("0000000000000001000100011011011010101111111110101010101001011")
    print(compressed_bit)
