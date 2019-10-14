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

