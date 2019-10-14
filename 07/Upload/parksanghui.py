### Homework 2 ###
tu = ('apple', [7,5,6], (1,2,3))
print("original : tu =", tu)

# convert the tuple 'tu' to a list 'li'
li = list(tu)
print("casting : li =", li)

# convert the list 'li' to a new tuple 'tu2'
tu2 = tuple(li)
print("converted tuple :", tu2)

# change the value of convertible tu2[1][1] to 20
tu2[1][1] = 20
print("tu2[1][1]=20, result :", tu2)

# Compute the sum of the first two element of 'tu2' and assign it to 'tu2[1][2]'
tu2[1][2] = sum(tu2[1][0:2])
print("sum(tu2[1][0:2]), result :", tu2)





### Lab 1 ###
count_iteration = 5

print("Let's make a dinner time!!!")
print("You must enter {iteration} {times}!!!".format(
    iteration = count_iteration,
    times = "time" if count_iteration < 2 else "times"
))

dlist = []

current_input = ""
i = 0
while True:
    current_input = input("Please enter a dinner ingredient : ")
    if current_input == "quit":
        break
    dlist.append(current_input)
    i += 1

dlist.sort()

for i, value in enumerate(dlist):
    print(i+1, value)






### Lab 2 ###
words = ["seoul", "tokyo", "moskoba", "toronto", "queensland", "beijing", "rome"]

longerthan5 = [ value for value in words if len(value) > 5 ]
longerthan5len = [ len(value) for value in words if len(value) > 5 ]

print("satisfy name\t:", longerthan5)
print("satisfy length\t:", longerthan5len)





### Lab 3 ###
voted = {
    "John": True,
    "Alice": False,
    "Rosa": True
}

print(voted)

while True:
    your_name = input("Enter your name : ")

    if your_name == "":
        # Terminate Program
        print(voted)
        break
    
    if voted.get(your_name):
        print(your_name,"already voted!")
    elif your_name in voted.keys():
        print(your_name+",","please vote!")
        voted[your_name] = True
    else:
        print(your_name,"has no voting rights.")
        
    '''
    in_voted = False
    did_I_vote = False
    
    for name in voted.keys():
        if name == your_name:
            in_voted = True
            did_I_vote = voted[name]


    if not in_voted:
        print(your_name,"has no voting rights.")
    elif did_I_vote:
        print(your_name,"already voted!")
    else:
        print(your_name+",","please vote!")
        voted[your_name] = True
    '''

    print()





### Lab 4 ###
aset = set()
bset = set()

a = int(input("1.Please enter a number : "))
b = int(input("2.Please enter a number : "))

aset = { i for i in range(1,a+1) if a % i == 0 }
print(aset)

bset = { i for i in range(1,b+1) if b % i == 0 }
print(bset)

print("Common factor :", aset & bset)





### Lab 5 ###
import random

rps = ["rock", "paper", "scissors"]

result = {
    ("rock", "paper"): False,
    ("rock", "scissors"): True,
    ("paper", "scissors"): False,
    ("paper", "rock"): True,
    ("scissors", "rock"): False,
    ("scissors", "paper"): True
}

while True:
    player = input("rock/paper/scissors : ")

    com = random.choice(rps)

    if not player in rps:
        if player == "":
            break
        
        print("invalid input!")
        print()
        continue

    print("player --->", player)
    print("computer --->", com)

    print("It's a tie" if player == com else "You won! :)" if result[(player, com)] else "You lost! :(")
    print()

    



