print('Function')

# hello()

def hello():
    print("hello world")


def hello():
    print("hello world")
hello()

def hello():
    print("hello world")
print(hello())


def math():
    return[1,9]
print(math())

def math():
    return[1,9],9
print(math())

def math():
    return[1,10],9
math()

def add ():
    return 10+20
print((add))

def add (a,b):
    return a+b
print(add(1,10))
print(add(20,33))

def user_info(fname, lname):
    return f'my name is {fname} {lname}'

print(user_info("Sharma","hari"))
print(user_info("hari", "Sharma"))
print("Keyword agruments")
print(user_info(lname="Sharma",fname="Hari"))

# def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
#     print("code here")


# calculate_fine("python",10,5,10) # 50
# calculate_fine("html",1.9,5,10) # error number should in int
# calculate_fine("html",1,"5",0) # error number should in int


def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
    if isinstance(borrowed_days,int) and isinstance(allowed_days, int):
        if not (borrowed_days<allowed_days):
            return {
                "fine":(borrowed_days-allowed_days)* fine_per_day,
                "book":book_name,
                "total_fine_days":borrowed_days-allowed_days
            }

        else:
            return{
                "fine":0,
                "book":book_name

            }

    else:
        return "Error number shoud be in int"



print(calculate_fine("python",10,5,10)) # 50
print(calculate_fine("html",1,5,10)) # 50

print(calculate_fine("html",1.9,5,10)) # error number should in int
print(calculate_fine("html",1,"5",0)) # error number should in int