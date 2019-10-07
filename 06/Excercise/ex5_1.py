test = [57, 99, 78, 85, 60]

for index, score in enumerate(test):
    print(
        "No.{humanReadableIndex} your score is {score}, {pf}!".format(
            humanReadableIndex = index+1,
            score = score,
            pf = "pass" if score >= 70 else "fail"
        )
    )
