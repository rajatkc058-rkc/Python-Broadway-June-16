i = 1
while (i==2):
    print(i)
    i=i+1 
    break


i = 1
while (i<=10):
    print(i)
    i=i+1


i = 10
while (i<=20):
    print(i)
    i=i+1

#random library
# import random
# print(random.random()) #0-1
# random.randint(20,100)

# c =[4,5,6,"test",3,4,5,6]
# print(random.choice(c))




import random
random_num = random.randint(1,10)
count = 0
lives = 5
while True:
    if count > lives - 1:
        print("no attempt left")
        # user_input = input("do you want to play again y/n ").lower()
        # if user_input == "y":
            # random_num = random.randint(1, 10):
            # print("random number is ", random_num)
            # count = 0
        # else:
        #     print("Thank you playing")
        break
    print(f"Remaining attempt", lives - count)
    count = count + 1
    user = int(input("enter a number"))
    if user == random_num:
        print("guessed successfully")
        print("attempt", count)
        user_input = input("do you want to play again y/n ").lower()
        if user_input == "y":
            random_num = random.randint(1, 10)
            print("random number is ", random_num)
            count = 0
        else:
            print("Thank you playing")
            break
    else:
        print("Try Again")
        