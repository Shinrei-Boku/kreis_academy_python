#class プロパティー2 lesson06.py

class Person(object):
    def __init__(self,name,age):
        print("create new Person")
        self.__name = name
        self.__age = age

    def myname(self):
        print("my name is {}".format(self.__name))

    def myage(self):
        print( "{}の{}歳です。".format(self.__name,str(self.__age)))

    def __del__(self):
        print("bye")

if __name__ == "__main__":
    person_kon = Person("kondo",20)
    person_kon.myname()
    person_kon.myage()

    person_kon.__age == 30
    print(person_kon.__age)

    person_kon.myage()