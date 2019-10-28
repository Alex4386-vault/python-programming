
def func_sum(*a):
    total = 0
    for i in a:
        total += i
    return total

score = [73, 95, 80, 57, 99]
sumscore = func_sum(*score)
print("Total score :", sumscore)
print("Average score :", sumscore/len(score))
