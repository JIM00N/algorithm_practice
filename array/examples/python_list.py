l = []

a = "string"
print('l = []\na = "string"\n위와 같이 초기화했다.\n')
print('a의 주소 : {}'.format(id(a)))
print('리스트 l의 주소 : {}'.format(id(l)))

l.append(a)
l.append(a)

print('\n"a"는 l에 두번 append되었다.\n')
print("TEST 111 ====")
print("print(l[0]) : {}".format(l[0]))
print("print(l[1]) : {}".format(l[1]))


print("\nTEST 222 ====\na='test'")
a = "test"
print('a의 주소 : {}'.format(id(a)))



print("print(id(l[0])) : {}".format(id(l[0])))
print("print(id(l[1])) : {}".format(id(l[1])))


print("print(l[0]) : {}".format(l[0]))
print("print(l[1]) : {}".format(l[1]))


print("\nclass를 이용한 예시도 알아보자.\nTEST 333 ====")

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

print("obj1 = A(10), obj1의 주소 : {}".format(id(obj1)))
print("l2 = [], l2의 주소 : {}".format(id(l2)))

print("l2[0]과 l2[1] 모두 obj1")
print("l2[0]의 주소 : {}, l2[0]의 값 : {}".format(id(l2[0]), l2[0].get_i()))
print("l2[1]의 주소 : {}, l2[1]의 값 : {}".format(id(l2[1]), l2[1].get_i()))

print("\nTEST 444 ====")

l2[0].set_i(20)
print('l2.set_i(20)')
print('id(obj1) : {}'.format(id(obj1)))
print('id(l2) : {}'.format(id(l2)))
print('id(l2[0]) : {}, l2[0].get_i() : {}'.format(id(l2[0]), l2[0].get_i()))
print('id(l2[1]) : {}, l2[1].get_i() : {}'.format(id(l2[1]), l2[1].get_i()))
