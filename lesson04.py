#class オーバライド、super lesson04.py

from lesson02 import Person

class Employees(Person):

    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number = number

    def mynumber(self):
        print("社員番号は {}　です。".format(self.number))

#if __name__ == "__main__":
employees_kon = Employees("kondo",20,"001")
employees_kon.myname()
employees_kon.myage()
#employees_kon.empno("001")
employees_kon.mynumber()