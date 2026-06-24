a={
    'name':'Hari',
    'address':'Nepal',
    'age': 22,
    'name':'Ram'
}

print(a)
print(type(a))
print(len(a))

print(a['name'])
#print(a['namea'])

a['address']='KTM'
a['Phone']=980

data= {
    'name':'sudan',
    'role':'developer'
}
a.update(data)
print(a)


data = {
    "name" : "Sudan",
    "phone" : [
        {"type":"NTC","number":9844},
        {"type":"Ncell","number":9806}
    ],
}
#Sudan NTC number is 9844
#Sudan Ncell number is 9806
print (data['name'], data['phone'][0]['type'], 'number is ', data['phone'][0]['number'])

print(f"{data['name']} {data['phone'][0]['type']} number is {data['phone'][0]['number']}")

dictionary= ["del , clear, pop pop.item"]
print(dictionary)




