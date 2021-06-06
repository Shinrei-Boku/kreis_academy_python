#class 継承 lesson03.py

from lesson02 import Person

class Employees(Person):

    def empno(self,number):
        self.number = number

    def mynumber(self):
        print("社員番号は {}　です。".format(str(self.number)))

#if __name__ == "__main__":
employees_kon = Employees("kondo",20)
employees_kon.myname()
employees_kon.myage()
employees_kon.empno("001")
employees_kon.mynumber()


