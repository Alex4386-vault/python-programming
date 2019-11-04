import math
import random

for i in range(2):
    print(random.random())

for i in range(2):
    rnd = random.randint(1,10)
    print(rnd,"->",math.pow(rnd,2))

fruits = ['apple', 'pear', 'lemon', 'banana']
for i in range(3):
    print(random.choice(fruits), end=' ')

print()