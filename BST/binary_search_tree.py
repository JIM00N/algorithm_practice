# 24.10.08

class bst:
    def __init__(self, max_level):
        self.tree = [None] * (2 ** max_level)

    def insert(self, n):
        cur_id = 1

        while self.tree[cur_id] != None:
            if n > self.tree[cur_id]:
                cur_id = 2 * cur_id + 1

            elif n < self.tree[cur_id]:
                cur_id = 2 * cur_id
            
            else:
                raise Exception("Duplication")
        
        self.tree[cur_id] = n
        
    def search(self, n):
        cur_id = 1

        while self.tree[cur_id] != None:
            if n > self.tree[cur_id]:
                cur_id = 2 * cur_id + 1
            elif n < self.tree[cur_id]:
                cur_id = 2 * cur_id
            else:
                return cur_id
        return None

    def delete(self, n):
        idx = self.search(n)
        if idx != None:
            left_child = self.tree[idx * 2] 
            right_child = self.tree[idx * 2 + 1] 
            self.tree[idx] = None # case 1
            if left_child != None or right_child != None:
                # case 2
                if left_child != None:
                    tmp_idx = idx * 4 + 1
                    self.tree[n] = left_child
                

        else:
            raise Exception("Not Exist")
    

if __name__ == "__main__":
    my_bst = bst(5)
    my_bst.insert(7)
    my_bst.insert(3)
    my_bst.insert(8)
    my_bst.insert(1)
    my_bst.insert(5)
    my_bst.insert(10)
    my_bst.insert(6)
    my_bst.delete(6)
    
    
    print(my_bst.tree)
    print(my_bst.search(5))
    print(my_bst.search(4))

    my_bst.delete(4)