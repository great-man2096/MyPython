class Washer:
    # 类型java的构造器
    def __init__(self,a,b):
        self.type = a
        self.kwh = b

    def __str__(self):
        return  "相当于java的toString方法"

    def __del__(self):
        print(f'对象已经被删除')

    @staticmethod
    def d():
        print("甩干")

    @staticmethod
    def wash():
        print("开始洗衣服")


# myWasher = Washer('海尔',1000)
#
# myWasher.wash()
# myWasher.d()
# # myWasher.type = '海尔'
# # myWasher.kwh = 1000
# print(myWasher.type)
# print(myWasher.kwh)

myWasher2 = Washer('xiaoHong',2000)

myWasher2.wash()
myWasher2.d()
# myWasher.type = '海尔'
# myWasher.kwh = 1000
print(myWasher2.type)
print(myWasher2.kwh)

print(myWasher2)
# del myWasher2