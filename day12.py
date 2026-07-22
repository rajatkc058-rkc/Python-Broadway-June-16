#lambda
n= lambda a,b : a+b
print(n(1,2))

# def add (a,b):
#     return a+b
# print(add(1,2))

#list comperhesion
a=[1,2,3,4,5]
# result =[]
# for in a:
#     result.append (i*i)
# print(result)


result = [i*i for i in a]
print(result)

square = lambda *args:[i**2 for i in args]
print(square(1,2,3,4,4,10))

print("---"*50)


#Class