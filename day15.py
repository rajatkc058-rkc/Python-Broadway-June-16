#multilevel
class A():
    a = 2
class B(A):
    b = 3
class C(B):
    c = 10
print(C.__mro__)

from datetime import datetime
class Book():
  def __init__(self,title,author,price,ISBN):
    self.title = title
    self.author = author
    self.price = price
    self.ISBN = ISBN
class BorrowedBook(Book):
  def __init__ (self, title, author, price, ISBN, b_name, b_date, d_date, a_days):
    self.borrower_name = b_name
    self.borrowed_date = b_date
    self.due_date = d_date
    self.allowed_days = a_days
    super().__init__(title,author,price,ISBN)

class LateBorrowedBook(BorrowedBook):
  def __init__(self,title,author,price,ISBN,b_name,b_date,d_date,a_days,r_date,l_fine,d_charge,is_damage):
    self.return_date = r_date
    self.late_fine = l_fine
    self.damage_charge = d_charge
    self.damage = is_damage
    super().__init__(title,author,price,ISBN,b_name,b_date,d_date,a_days)

  def late_days(self):
    date_format = "%Y/%m/%d"
    b = datetime.strptime(self.due_date,date_format)
    r = datetime.strptime(self.return_date,date_format)
    return (r - b).days
  def calc_fine(self):
    return self.late_days()*self.late_fine
  def calc_total (self):
    if self.damage == True:
      return self.calc_fine()+self.damage_charge
    else:
      return self.calc_fine()+0
  def display(self):
      return f''' Title :{self.title}
      Author : {self.author}
      Price :{self.price}
      ISBN :{self.ISBN}
      B-name :{self.borrower_name}
      B-date : {self.borrowed_date}
      D-date : {self.due_date}
      A-days : {self.allowed_days}
      R-date : {self.return_date}
      fine_prday : {self.late_fine}
      D-charge :{self.damage_charge}
      late days :{self.late_days()}
      fine : {self.calc_fine()}
      Totalpay :{self.calc_total()}'''
obj = LateBorrowedBook("PythonProgram","Hari",900,12456,"Rom","2083/02/15","2083/03/14",30,"2083/03/20",50,400,True)
# print(obj.late_days())
# print(obj.calc_fine())
# print(obj.calc_total())
print(obj.display())

