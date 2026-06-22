a = 10
print(type(a))


marks = 80 #(if)
if (marks>=80 and marks<=100):
    print("Dis")
elif (marks>=60):
    print("first")
else:
    print('fail')


marks = int(input("enter the marks"))#(nested if)
if (marks>=80 and marks<=100):
    print("Dis")
    if marks==100:
        print('Topper')
    elif(marks==80):
        print("lucky")
elif (marks>=60 and marks<=79):
    print("first")
else:
    if marks == 59:
        print('unlucky')
    print('fail')


monthlyincome = int(input('enter the monthly income:'))
creditscore = int(input('enter the credit score:'))
#Gurantor = input("Do you have a gurantor (Y/N):")
if(monthlyincome>=3000):
    if creditscore >=700:
       print("loan approved")
    else:
        print("Reject")
elif( monthlyincome <3000):
    if creditscore>= 750:
        Gurantor = input("Do you have a gurantor (Y/N):")
        if(Gurantor== 'Y'):
            print("approve loan")
        else:
            print('Reject')
    else:
        print('Reject')
else:
    print('reject')

















 