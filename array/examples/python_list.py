l = []

a = "string"
print(id(a))

l.append(a)
l.append(a)

print(id(l))

print("TEST 111 ====")
print(id(l[0]))
print(id(l[1]))


print("TEST 222 ====")
a = "test"
print(id(a))

print(id(l[0]))
print(id(l[1]))

print(l[0])
print(l[1])

print("TEST 333 ====")
###
class A:
    def __init__(self, i):
        self.i = i
        
    def set_i(self, i):
        self.i = i

    def get_i(self):
        return self.i

l2 = []
obj1 = A(10)

l2.append(obj1)
l2.append(obj1)

print(id(obj1))
print(id(l2))
print(id(l2[0]), l2[0].get_i())
print(id(l2[1]), l2[1].get_i())

print("TEST 444 ====")

l2[0].set_i(20)
print(id(obj1))
print(id(l2))
print(id(l2[0]), l2[0].get_i())
print(id(l2[1]), l2[1].get_i())


