for i in [1,2,3,4,5]:
    print(i)

for z in "boradway":
    print(z)

a = {
    "name": "ram",
    "address": "nepal"
}

for i in (a):
  print(i)

for i in a.values():
   print(i)

for i in a:
    print(i,a[i])

for i in a:
    print(a,[i])



for i in range (1,11,1):
   n=9
   if i == 6:
      break
   print(f'{n}*{i}={n*i}')

print("----"*20)
for i in range (1,11,1):
   n=9
   if i == 6:
      continue
   print(f'{n}*{i}={n*i}')


#nested loop

for i in range (1,5,1):
   for j in range (2,5):
      print(i,j)

a = [10,20,10,20]
for i in set (a):
   for j in range (1,11,1):
      print (f'{i}*{j}= {i*j}')
print('\n')


x = []
for b in range(1,6):
   y = int(input(f"enter the {b} number:"))
   x.append(y)
print(x)
print(type(x))

for i in set(x):
   for j in range (1,11):
      print(f"{i} X {j} = {i*j}")

   print("\n")