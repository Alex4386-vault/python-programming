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
            exit()
        
        print("invalid input!")
        print()
        continue

    print("player --->", player)
    print("computer --->", com)

    print("It's a tie" if player == com else "You won! :)" if result[(player, com)] else "You lost! :(")
    print()

    




