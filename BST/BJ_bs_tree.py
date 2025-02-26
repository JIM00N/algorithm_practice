# Problem : [이진 검색 트리] https://www.acmicpc.net/problem/5639
# Solver : 문지석
# Solved Date : 2025.02.05
# BigO : N * log(N)
import sys
input = sys.stdin.readline

class BST:
    def __init__(self):
        self.po_list = []

    def post_order(self, tmp_tree, start=0):
        if len(tmp_tree) == 1:
            self.po_list.append(f"{tmp_tree[start]}")
            return

        root = tmp_tree[start]  # pre_order로 주어지니 root는 가장 앞

        # 인덱스 초기화
        left_child_idx = 1
        right_child_idx = len(tmp_tree)

        # LC와 RC를 찾고, 나눠주자
        for idx, node in enumerate(tmp_tree):
            if node > root:
                right_child_idx = idx
                break
            if node < root and left_child_idx == 0:
                left_child_idx = idx

        tmp_left = tmp_tree[left_child_idx:right_child_idx]
        tmp_right = tmp_tree[right_child_idx:]

        if len(tmp_left) != 0 and len(tmp_right) != 0:
            # 양쪽 자식 트리가 모두 있을 때
            self.post_order(tmp_left)  # 왼쪽 먼저, post_order
            self.post_order(tmp_right)
        elif len(tmp_left) == 0 and len(tmp_right) != 0:
            # 오른쪽만 있을 때
            self.post_order(tmp_right)
        elif len(tmp_left) != 0 and len(tmp_right) == 0:
            # 왼쪽만 있을 때
            self.post_order(tmp_left)

        self.po_list.append(f"{root}")  # 자식들 추가한 뒤에 root 추가


if __name__ == "__main__":
    pre_order = []

    while True:
        try:
            pre_order.append(int(input().strip()))
        except:
            break

    pre_to_post = BST()
    pre_to_post.post_order(pre_order)
    print("\n".join(pre_to_post.po_list))
