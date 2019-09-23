total = 0

for i in range(5):
    score = int(input("enter the score of subject {0}: ".format(i+1)))
    total += score

score = total / 5

a = (score // 10) - 9

if not a or a == 1:
    print("A")
elif not (a+1):
    print("B")
elif not (a+2):
    print("C")
elif not (a+3):
    print("D")
else:
    print("F")