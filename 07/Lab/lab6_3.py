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
        exit()

    if your_name in voted.keys():
        if voted[your_name]:
            print(your_name,"already voted!")
        else:
            print(your_name+",","please vote!")
            voted[your_name] = True
    else:
        print(your_name,"has no voting rights.")


    print()