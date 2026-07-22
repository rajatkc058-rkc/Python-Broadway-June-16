import random
computer_num = random.randint(1,5)
print("Computer number is",computer_num)
attempt = 0
life = 5
while True:
  if attempt > life-1:
    print("No life left")
    break
  print ("Remaining life is",life-attempt)
  attempt = attempt+1
  users_guess = int(input('enter the number you guessed:'))
  if users_guess == computer_num:
    print("Congratulations you win!!")
    print("You guessed at attempt:",attempt)
    ask_user = input("Do you like to continue y/n:")
    if ask_user == 'y':
      computer_num = random.randint(1,5)
      print("Computer number is",computer_num)
      attempt = 0
    else:
      print("Thank you for playing")
      break
  elif users_guess > computer_num:
    print("Higher")
  else:
   print("Lower")


import random
A = ["Scissor","Paper","Rock"]
B = random.choice(A)
print("B:",B)
attempt = 0
life = 3
while True:
  if attempt > life - 1:
    print("Life Finished")
    break
  print("Remaining life",life-attempt)
  attempt  = attempt + 1
  user = input("Enter the guess:")
  if user =="Paper" and B == "Rock" or user == "Rock" and B =="Scissor" or user == "Scissor" and B == "Paper":
    print("User_Wins")
    print("You win at attempt",attempt)
    ask_user = input("Do you like to play again y/n:").lower()
    if ask_user == "y":
      B = random.choice(A)
      print("B:",B)
      attempt = 0
    else:
      print("Thank you for playing")
      break
  elif user == B:
    print("Draw")
  else:
    print("loss")