# class について lesson02.py
class Person(object):
    def __init__(self,name,age):
        print("create new Person")
        self.name = name
        self.age = age

    def myname(self):
        print("my name is {}".format(self.name))

    def myage(self):
        print( "{}の{}歳です。".format(self.name,str(self.age)))

    def __del__(self):
        print("bye")

if __name__ == "__main__":
    person_kon = Person("kondo",20)
    person_kon.myname()
    person_kon.myage()

