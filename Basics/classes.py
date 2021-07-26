import functions


class Animal:
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def speaks(self):
        print(f'{self.__name} speaks')


class Dog(Animal):
    def __init__(self, name=None, age=None):
        super().__init__(name, age)
        self.__name = name  # Private member
        self.__age = age

    def speaks(self):
        print(f'{self.__name} bhow bhow')

    def birthday(self):
        self.__age = self.__age + 1

    def getName(self):
        return self.__name


d1 = Dog('d1', 5)
print(f'{d1.getName()}')
print(f'{d1} {type(d1)}')
d1.speaks()
d1.birthday()
d2 = Animal('d2', 2)
d2.speaks()
functions.fun1(2)
functions.fun1()
