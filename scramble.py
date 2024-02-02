from numpy import random

possibleMoves = ["r", "r'",
                 "l", "l'",
                 "u", "u'",
                 "d", "d'", 
                 "f", "f'", 
                 "b", "b'",]
scramble = []

for i in range(random.randint(20)):
    scramble.append(possibleMoves[random.randint(12)])
    

print(scramble)