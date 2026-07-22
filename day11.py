def add(*args):
    total = 0
    for i in args:
        total = total +i
    return total



print(add(1,2,"sudna","tets"))
print(add(1,2,3))
print(add(1,2,3,4))
print(add())


def add(*args):
    if len(args)==0:
        return "Please provide any number"
    total = 0
    for i in args:
        if isinstance (i, int):
            total = total +i
    return total



print(add(1,2,"sudna","tets"))
print(add(1,2,3))
print(add(1,2,3,4))
print(add())


def all (*args, **Kwargs):
    print(*args)
    print(Kwargs)

all(1,2,3,4,'Hari','tests',1,1,name="Rajat")
all(1,2,3,4,"hari","tests",1,1)


def all (a,*args, **Kwargs):
    print(a)
    print(*args)
    print(Kwargs)

all(1,2,3,4,'Hari','tests',1,1,name="Rajat")
all(1,2,3,4,"hari","tests",1,1)
all(0)


# def marksheet(student_name, *subjects, **extra):
#     total = 0
#     for i in subjects:
#         total = total + i[1]
#         # total += i[1]
#     return (f"{student_name}'s total marks is {total} and percentage is {total/len(subjects)} and class teacher is {extra.get('class_teacher')}")




# print(marksheet(
#     "Sudan Bhandari",
#     ("Mathematics", 92),
#     ("Science", 88),
#     ("English", 85),
#     ("Social Studies", 81),
#     class_teacher="Mr. Sharma",
#     grade_level="Grade 10",
#     attendance="96"
# ))



def area (r, pie=3.14):
    return pie*r*r
print(area(1))
print(area(7,5))


# def area (r=7, pie=3.14):
#     return pie*r*r
# print(area())
# print(area(7,5))

# def area (r=7, pie):
#     return pie*r*r
# print(area(1))
# print(area(7,5))

# def area (r, pie=3.14):
#     return pie*r*r
# print(area(1,3.14))
# print(area(7,5))
