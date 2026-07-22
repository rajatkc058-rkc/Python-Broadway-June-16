class Test():
    a = 10
    b = 15
obj = Test()
print(obj)
print(obj.a)
# print(obj.c)

# obj1 = Test()
# print(obj == obj1)


class Test():
    a = 10
    b = 15
obj = Test()
obj.a ="Changed"
obj.c = "new value"
print(obj.a)
print(obj.c)

obj1 = Test()
print (obj1.a)
# print(obj1.c)

class Test2():
    a = 10
    b = 15
    def add (self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    
obj = Test2()
print(obj.add())
obj.a = 5
print(obj.sub())



class Test2():
    a = 10
    b = 15
    def add (self,d):
        self.c = 100
        self.d = d
        return d+self.b
    
    def sub(self):
        print(self.d)
        return self.a-self.b
    
    def result (self):
        return self.add(10)+self.sub()
    
obj = Test2()
#print(obj.add(10))
# obj.a = 5
# print(obj.c)
print(obj.result())

class Test3():
    def __init__(self):
        print("testing")

obj = Test3()

class Test3():
    def __init__(self,a,b):
        print("testing")

obj = Test3(5,6)

# class Test3():
#     def __init__(self,a,b,c):
#         print("testing")
#         return 1

# obj = Test3(5,6)


#str
class Test4():
    a=10
    message = "testing-message"

    def __str__(self):
        return self.message
obj = Test4()
print(obj)

# def testing():
#     pass
# def testing():...

class Test5():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(a,b)
    def add(self):
        return self.a + self.b
obj = Test5 (50,1)
print(obj.add())



# 3. Library Book

# Create a Book class.

# Attributes:

# title
# author
# ISBN
# total_copies
# available_copies

# Methods:

# Borrow a book.
# Return a book.
# Check availability.
# Display book details.


class Book:
  def __init__(self,title, author, ISBN, total_copies, available_copies):
    self.Title = title
    self.Author = author
    self.ISBN = ISBN
    self.totalcopies = total_copies
    self.availabelcopies = available_copies
    print(title, author, ISBN, total_copies, available_copies)
  def borrow_book (self):
    if self.availabelcopies > 0:
      self.availabelcopies = self.availabelcopies -1
      return "Book Borrowed"
    else:
      return "Books are not available"
  def return_book (self):
    if self.availabelcopies < self.totalcopies:
      self.availabelcopies = self.availabelcopies + 1
      return "Books returned"
    else:
      return "Books are already in the library"
  def check_availability (self):
    return self.availabelcopies
  def display_details(self):
    return{
        "Title" : self.Title,
        "Author" : self.Author,
        "ISBN": self.ISBN,
        "Totalcopies": self.totalcopies,
        "Availablecopies": self.availabelcopies

    }

object = Book ("International_Business","RajatKC",98456,20,20)
print(object.borrow_book())
print(object.return_book())
print(object.check_availability())
print(object.display_details())