test = [
    [ 75, 90, 66, 100, 50 ],
    [ 80, 92, 78, 90, 84 ]
]

subject = [ "English", "Math" ]

for subjectIndex, scores in enumerate(test):
    average = sum(scores) / len(scores)
    print("{subject} Average : {average}".format(
        subject = subject[subjectIndex],
        average = average
    ))