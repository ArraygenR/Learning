class person:
    totalObjects=0

    def __init__(self,name= "ABC"):
        self.__name = name
        person.totalObjects = person.totalObjects + 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting..')
        person.totalObjects = person.totalObjects - 1
        del self.__name

    @classmethod
    def showcount(cls):
        print("Total objects: ",cls.totalObjects)

    @staticmethod
    def greet():
        print("Hello!")


p1 = person()
print(p1.name)
person.showcount()
del p1.name
person.showcount()
person.greet()