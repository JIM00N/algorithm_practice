# Problem : [축사 배정] https://www.acmicpc.net/problem/2188
# Solver : 문지석
# Solved Date : 2025.02.07
# BigO : n ** 2


class cage:
    def __init__(self, cow_cage, apply):
        self.num_cows, self.num_cages = cow_cage
        self.apply = apply
        self.cows_connected = {i: None for i in range(1, self.num_cows + 1)}
        # 축사에 연결된 소 표시
        self.cages_connected = {i: None for i in range(1, self.num_cages + 1)}
        # 임자있는 축사 표시
        self.visit = {i: 0 for i in range(1, self.num_cages + 1)}
        # {축사번호: 방문한 소 번호(0으로 초기화), ...} 방문 처리
    
    def assign(self, id, prev=False): 
    # id는 소의 번호
    # 임자있는 축사에 배정됐을 때에 재귀를 실행했다는 것을 표시하기 위한 prev

        if prev == False: 
            # 재귀가 실행되지 않았다면 self.visit 초기화, 모든 축사에 접근 가능
            self.visit = {i: 0 for i in range(1, self.num_cages + 1)}

        for cage in self.apply[id - 1]: # 한 소가 지원한 축사들 loop
            
            if self.cages_connected[cage] == None: 
                # 지원한 축사에 배정된 소가 없다면 할당(재귀 여부와 관계 없이 지원한 축사가 비었다면)
                self.cages_connected[cage] = id
                self.cows_connected[id] = cage
                break

            elif prev == False:
                # 재귀가 실행되지 않았다면 먼저 방문처리
                self.visit[cage] = id
                if self.is_able_to_go(self.cages_connected[cage]):
                    # self.cages_connected[cage] -> the ID of cow assigned first
                    # 이미 케이지에 할당되어 있던 소가 다른 곳에 갈 수 있는지 확인하고
                    # 가능하다면 다른 곳으로 보내자
                    self.assign(self.cages_connected[cage], True)
                    break

            elif prev == True:
                # 쫓겨난 소가 갈 곳이 없으면
                for i in range(1, self.num_cages + 1):
                    if self.visit[i] != 0: # 굴러온 소가 방문한 케이지에 굴러온 소 할당
                        self.cages_connected[i] = self.visit[i]
                        self.cows_connected[self.visit[i]] = i
                break

    def is_able_to_go(self, id):
        for cage in self.apply[id - 1]:
            if self.cages_connected[cage] == None:
                self.visit[cage] = id
                return True
            elif self.visit[cage] == 0:
                self.visit[cage] = id
                if self.is_able_to_go(self.cages_connected[cage]):
                    return True
        
        return False
    
    def count(self):
        num_assigned = 0
        for i in range(1, self.num_cows+1):
            if self.cows_connected[i] != None:
                num_assigned += 1
        
        return num_assigned

if __name__=="__main__":
    num_cows, num_cages = tuple(map(int, input().split()))
    apply_list = [] # [[cage #x, cage #y, ...], [cage #k, cage #l, ...], ...]
    # 소의 수만큼 리스트가 포함되고 소의 번호 순대로 리스트가 들어감.
    for i in range(num_cows):
        apply_list.append(list(map(int, input().split()))[1:])

    cows_room = cage((num_cows, num_cages), apply_list)
    for i in range(1, num_cows+1):
        cows_room.assign(i)

    print(cows_room.count())
