#class 抽象クラス lesson07.py

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self,name,age):
        print("create new Person")
        self.__name = name
        self.__age = age

    def myname(self):
        print("my name is {}".format(self.__name))

    def myage(self):
        print( "{}の{}歳です。".format(self.__name,str(self.__age)))

    @abc.abstractmethod
    def department(self):
        pass

    def __del__(self):
        print("bye")


class KreisPerson(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.__department = "kreis"

    def department(self):
        print("所属は{}".format(self.__department))


kon = KreisPerson("kondo","20")
kon.myname()
kon.myage()
kon.department()