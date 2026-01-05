# Problem : [축사 배정] https://www.acmicpc.net/problem/2188
# Solver : 문지석
# Solved Date : 2025.02.07
# BigO : n ** 2


class cage:
    def __init__(self, cow_cage, apply):
        self.num_cows, self.num_cages = cow_cage
        self.apply = apply
        self.cows_connected = {i: None for i in range(1, self.num_cows + 1)}
        self.cages_connected = {i: None for i in range(1, self.num_cages + 1)}
        self.visit = {i: False for i in range(1, self.num_cages + 1)}
    
    def assign(self, id, prev=False):
        if prev == False:
            self.visit = {i: False for i in range(1, self.num_cages + 1)}

        for cage in self.apply[id - 1]:
            
            if self.cages_connected[cage] == None:
                self.cages_connected[cage] = id
                self.cows_connected[id] = cage
                break

            elif prev == False:
                self.visit[cage] = id
                if self.is_able_to_go(self.cages_connected[cage]):
                    self.assign(self.cages_connected[cage], True)
                    break

            elif prev == True:
                for i in range(1, self.num_cages + 1):
                    if self.visit[i] != False:
                        self.cages_connected[i] = self.visit[i]
                        self.cows_connected[self.visit[i]] = i
                break

    def is_able_to_go(self, id):
        for cage in self.apply[id - 1]:
            if self.cages_connected[cage] == None:
                self.visit[cage] = id
                return True
            elif self.visit[cage] == False:
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
    apply_list = []
    for i in range(num_cows):
        apply_list.append(list(map(int, input().split()))[1:])

    cows_room = cage((num_cows, num_cages), apply_list)
    for i in range(1, num_cows+1):
        cows_room.assign(i)

    print(cows_room.count())
