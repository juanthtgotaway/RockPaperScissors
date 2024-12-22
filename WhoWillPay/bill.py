import random

friends = ["Juan", "Paola", "Jason", "Erick", "Stephanie", "David", "Christa"]

print(random.choice(friends))

# Other options: 
randomName = random.randint(0,7)
print(friends[randomName])
