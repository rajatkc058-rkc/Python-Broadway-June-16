# git checkout main
# aborting
# git reset --hard
# git stash
# git stash pop 
# git branch
# *main
# git pull origin main


#inheritance

class Parent():
    a = 20
    d = 100

class Child(Parent):
    a = 11
    b = "Hari"
obj = Child()
print(obj.b)
print(obj.d)
print(obj.a)


class Parent():
    a = 20
    d = 100

    def display (self):

        return "Display from parent class"

    def add (self):

        return self.a +self.c
class Child(Parent):
    a = 11
    b = "Hari"
    c = 10
obj = Child()
# print(obj.b)
# print(obj.d)
# print(obj.a)

print(obj.display())
print(obj.add())


class Parent():
    a = 20
    d = 100

    def __init__(self):
        print('from parent')

    def display (self):

        return "Display from parent class"

    def add (self):

        return self.a +self.c
class Child(Parent):
    a = 11
    b = "Hari"
    c = 10

    def __init__(self):
        print("From child")
        #parent.__init__(self)
        super().__init__()
        print(super().a)
obj = Child()


class Employee():
    def __init__(self,id,name,salary):
        self.employee_id = id
        self.name = name
        self.basic_salary = salary



class PermanentEmployee(Employee):
    def __init__(self,id,name,salary,bonus,tax):
        self.bonus = bonus
        self.tax = tax
        super().__init__(id,name,salary)


    def calc_gross_salary(self):
      return self.basic_salary + self.bonus

    def tax_amount (self):
      return self.calc_gross_salary() * 0.15

    def net_salary(self):
      return self.calc_gross_salary()-self.tax_amount()


    def all_employee_detail(self):
      print("Employee_Details")
      return f'''
      employee_id: {self.employee_id}
      name: {self.name}
      basic_salary:{self.basic_salary}
      bonus:{self.bonus}
      tax_percentage :{self.tax}
      gross_salary: {self.calc_gross_salary()}
      tax_amount: {self.tax_amount()}
      net_salary:{self.net_salary()}'''
      


obj = PermanentEmployee(134, "Ram",10000, 1000,15)
print(obj.all_employee_detail())



