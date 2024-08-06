class MyStack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        return val
    def showall(self):
        for item in self.stack[::-1]:
            print(item)
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack)==0
    
    
if __name__=="__main__":
    stack = MyStack()
    print(f"stack.isEmpty() : {stack.isEmpty()}")
    for i in range(20):
        stack.push(i)
        print(f"stack.push({i})")
    print("====showall start====")
    stack.showall()
    print("====showall end====")
    for _ in range(5):
        print(f"stack.pop() : {stack.pop()}")
    print(f"stack.size() : {stack.size()}")
    print(f"stack.isEmpty() : {stack.isEmpty()}")
    print("====showall start====")
    stack.showall()
    print("====showall end====")
