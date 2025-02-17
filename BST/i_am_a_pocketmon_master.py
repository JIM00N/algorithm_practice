# Problem : [나는야 포켓몬 마스터 이다솜] https://www.acmicpc.net/problem/1620
# Solver : 문지석
# Solved Date : 2025.02.05
# BigO : N * log(N)
from dataclasses import dataclass


@dataclass
class Pocket_Mon:
    name: str
    num: int
    left_child: object = None
    right_child: object = None


class Pocketmon_Ball:
    def __init__(self):
        self.name_list = []
        self.root: Pocket_Mon = None

    def insert(self, mon: Pocket_Mon):
        self.name_list.append(mon)

        if len(self.name_list) == 1:
            self.root = mon
            return

        cur_mon = self.root
        while cur_mon != None:
            if cur_mon.name > mon.name:
                if cur_mon.left_child != None:
                    cur_mon = cur_mon.left_child
                else:
                    cur_mon.left_child = mon
                    return
            elif cur_mon.name < mon.name:
                if cur_mon.right_child != None:
                    cur_mon = cur_mon.right_child
                else:
                    cur_mon.right_child = mon
                    return

    def search_by_num(self, n: int):
        return self.name_list[n - 1].name

    def search_by_name(self, name: str):
        cur_mon = self.root
        while cur_mon.name != name:
            if cur_mon.name > name:
                cur_mon = cur_mon.left_child
            elif cur_mon.name < name:
                cur_mon = cur_mon.right_child

        return cur_mon.num


if __name__ == "__main__":
    num_pocketmons, num_questions = tuple(map(int, input().split()))
    lee_dasom = Pocketmon_Ball()

    for i in range(num_pocketmons):
        lee_dasom.insert(Pocket_Mon(input(), i + 1))

    result = []
    for _ in range(num_questions):
        question = input()
        try:
            question = int(question)
            result.append(lee_dasom.search_by_num(question))
        except:
            result.append(f"{lee_dasom.search_by_name(question)}")

    print("\n".join(result))
