# Problem : [이진 검색 트리] https://www.acmicpc.net/problem/5639
# Solver : 문지석
# Solved Date : 2025.02.05
# BigO : N * log(N)
import sys
input = sys.stdin.readline

class BST:
    def __init__(self):
        self.po_list = []

    def pre2post(self, tmp_tree):
        root = tmp_tree[0]  # pre_order로 주어지니 root는 가장 앞

        if len(tmp_tree) == 1:
            self.po_list.append(f"{tmp_tree[0]}")
            return
        
        # Left subtree와 right subtree가 나뉘는 idx 찾기
        cut_idx = 1

        for val in tmp_tree[1:]:
            if val > root: # right subtree가 나오는 순간 break
                break
            cut_idx += 1

        tmp_left = tmp_tree[1:cut_idx]
        tmp_right = tmp_tree[cut_idx:]

        if len(tmp_left) != 0 and len(tmp_right) != 0:
            # 양쪽 자식 트리가 모두 있을 때
            self.pre2post(tmp_left)  # 왼쪽 먼저, pre -> post
            self.pre2post(tmp_right)
        elif len(tmp_left) == 0 and len(tmp_right) != 0:
            # 오른쪽만 있을 때
            self.pre2post(tmp_right)
        elif len(tmp_left) != 0 and len(tmp_right) == 0:
            # 왼쪽만 있을 때
            self.pre2post(tmp_left)

        self.po_list.append(f"{root}")  # 자식들 추가한 뒤에 root 추가


if __name__ == "__main__":
    pre_order = []

    while True:
        try:
            pre_order.append(int(input().strip()))
        except:
            break

    pre_to_post = BST()
    pre_to_post.pre2post(pre_order)
    print("\n".join(pre_to_post.po_list))
