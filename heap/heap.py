class heap:
    def __init__(self, max_level):
        self.heap = self.tree = [None] * (2 ** max_level)
        self.next_pos = 0
    
    def push(self, number):
        if self.next_pos == 0:
            self.heap[0] = number
        
        else:
            aim_pos = self.next_pos
            self.heap[aim_pos] = number
            parent = (aim_pos - 1) // 2
            while self.heap[parent] < self.heap[aim_pos]:
                self.heap[parent], self.heap[aim_pos] = self.heap[aim_pos], self.heap[parent]
                if parent > 0:
                    aim_pos = parent
                    parent = (parent - 1) // 2

        self.next_pos += 1
    
    def find(self):
        return self.heap[0]

    def pop(self):
        last_pos = self.next_pos - 1
        return_val = self.heap[0]
        self.heap[0] = self.heap[last_pos]
        self.heap[last_pos] = None
        last_pos = 0
        while True:
            child_1 = self.heap[last_pos*2 + 1]
            child_2 = self.heap[last_pos*2 + 2]

            if child_1 != None and child_2 != None:
                if child_1 > child_2:
                    bigger_child = child_1
                else:
                    bigger_child = child_2

            elif child_1 != None:
                bigger_child = child_1
                
            elif child_2 != None:
                bigger_child = child_2

            else:
                break

            if bigger_child < self.heap[last_pos]:
                break
            
            idx_smaller_child = self.heap.index(bigger_child)
            self.heap[last_pos], self.heap[idx_smaller_child] = self.heap[idx_smaller_child], self.heap[last_pos]
            last_pos += 1

        self.next_pos -= 1
        return return_val


if __name__=="__main__":
    test = heap(4)
    
    test.push(10)
    test.push(5)
    test.push(3)
    test.push(2)
    test.push(4)
    test.push(15)
    test.push(13)
    test.push(132)
    test.push(192)
    test.push(43)
    test.push(151)
    print(test.heap)
        
    print(test.pop())
    print(test.pop())                   
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())


    print(test.heap)
    
    

    