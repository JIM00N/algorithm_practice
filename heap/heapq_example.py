import heapq

my_heap = []

heapq.heappush(my_heap, 578439)
heapq.heappush(my_heap, 4234)
heapq.heappush(my_heap, 32498340)
heapq.heappush(my_heap, 234)
heapq.heappush(my_heap, 239084)
heapq.heappush(my_heap, 33)
heapq.heappush(my_heap, 1)

print(my_heap)

print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))
 

my_list = [12, 3, 13, 34, 342, 64, 543, 66, 233, 111]
heapq.heapify(my_list)
print(my_list)
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
print(heapq.heappop(my_list))
