class SweetPotato():
    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiment = []

    def cook(self, time):
        """
        烤地瓜的方法
        :return:
        """
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    def add_condiments(self,condiment):
        """添加填料"""
        self.condiment.append(condiment)

    def __str__(self):
        return f'烤了{self.cook_time}分钟，现在地瓜状态现在是{self.cook_static},调料有{self.condiment}'


first = SweetPotato()
print(first)
first.cook(2)
print(first)
first.add_condiments("糖")
first.cook(2)
print(first)
first.add_condiments("盐")
first.cook(2)
print(first)
first.cook(2)
print(first)
