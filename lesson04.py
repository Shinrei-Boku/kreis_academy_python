#class オーバライド、super lesson04.py

from lesson02 import Person

class Employees(Person):

    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number = number

    def mynumber(self):
        print("社員番号は {}　です。".format(self.number))

    def myname(self):
        print("私は社員です。名前は{}です".format(self.name))

#if __name__ == "__main__":
employees_kon = Employees("kondo",20,"001")
employees_kon.myname()

person_kon =Person("kondo",20)
person_kon.myname()