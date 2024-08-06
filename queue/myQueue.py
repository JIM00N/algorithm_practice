class MyQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        temp = self.queue[0]
        self.queue = self.queue[1:]
        return temp
    def showall(self):
        for i in reversed(range(len(self.queue))):
            print(f"{self.queue[i]}", end=' ')
        print()
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue)==0
    
if __name__=="__main__":
    queue = MyQueue()
    print(f"queue.isEmpty : {queue.isEmpty()}")
    for i in range(20):
        queue.enqueue(i)
        print(f"queue.enqueue() : {i}")
    print("====showall start====")
    queue.showall()
    print("====showall finished====")
    for _ in range(5):
        print(f"queue.dequeue() : {queue.dequeue()}")
    print("====showall start====")
    queue.showall()
    print("====showall finished====")
    
    print("====deque test====")
    from collections import deque
    
    queue2 = deque([4,5,6])
    queue2.append(7)
    queue2.append(8)
    print(queue2)
    print(queue2.popleft())
    print(queue2.popleft())
    print(queue2)
