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

gameOps = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if userChoice >= 0 and userChoice <=2:
    print(gameOps[userChoice])
computerChoice = random.randint(0,2)
print (f'Computer Chose:')
print(gameOps[computerChoice])

if userChoice >= 3 or userChoice < 0:
    print("Invalid entry you lose!")
elif userChoice == 0 and computerChoice == 2:
    print("You win!")
elif computerChoice == 0 and userChoice == 2: 
    print("You Lose")
elif computerChoice > userChoice:
    print("You Lose!")
elif userChoice > computerChoice: 
    print("You Win!")
elif computerChoice == userChoice:
    print("Its a draw! Try again.")
else: 
    print("Invalid entry. You lose!")

