import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

select_Img=[rock,paper,scissors]
select_Nm=["Rock","Paper","Scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2:
    print("you loose, try again")
    exit()

print(f"You select : {select_Nm[user_choice]} \n" + select_Img[user_choice])
computer_choice =random.randint(0,2)
print(f"Computer select : {select_Nm[computer_choice]} \n" + select_Img[computer_choice])
# game decide

if user_choice ==  computer_choice:
    print("it is a draw")
elif (user_choice == 0 and computer_choice ==2) or (user_choice == 1 and computer_choice ==0) or (user_choice == 2 and computer_choice ==1) :
    print("You Own")
else:
    print("Computer Own")