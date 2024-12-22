import random

# randomInt=random.randint(1,10)
# print(randomInt)

# randomNumber = random.random()
# print(randomNumber)

# randomFloat = random.uniform(1,10)
# print(randomFloat)

# MyCode:
input('How lucky are you feeling? Pick heads or tails by responding "heads" or "tails\n').lower()
if input == "heads":
    compChoice = random.randint(1,2)
    if compChoice == 1:
        print('You\'re fate chose tails')
    else:
        print('You\'re fate chose heads')
else:
    compChoice = random.randint(1,2)
    if compChoice == 2:
        print('You\'re fate chose tails')
    else:
        print('You\'re fate chose heads')

# course answer
# compChoice = random.randint(0, 1)
# if compChoice == 0: 
#     print("Heads")
# else:
#     print("Tails")
