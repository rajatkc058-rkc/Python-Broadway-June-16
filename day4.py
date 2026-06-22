print('Hello world')


a=[1,2,3,4,5]
print(a)
print(type(a))


#4 to -5
print(a[0])

#print(a[-6]) index out of range

print(len(a))

a=[1,2,3]
a[0]=100
#a[9]=2
print(a)

a=[1,2,3,4,5,6,7,78]
print(a[3:5])
print(a[:5])
print(a[1:])
print(a[:])

print('----'*20)

#append
a = [1,2,3]
a.append(4)
print(a)

a=[]
a.append(2)
print(a)


#insert
a=[1,2,3,5,6]
a.insert(3,4)
a.insert(1,500)
a.insert(200,2)
print(a)

print('-----'*20)

#extend
a=[1,2,3]
b=[4,5,6]

a.extend(b)
print(a)
b.extend(a)
print(b)

#c=b.extend(a) cant be done
#print(c)

a=[1,2,3]
b=[4,5,6]

print(a+b)
c = a+b
c = a+b+a

print(c)



List_delete=["remove, delete, pop and clear"]
print(List_delete)