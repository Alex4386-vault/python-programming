# Short coding version
[ a for a in [[ int(input("Enter "+("first" if i == 0 else "second")+" number: ")) for i in range(0,2) ]] if print("quotient: "+str(a[0]//a[1])+", remainder: "+str(a[0]%a[1])) ]

first,second = int(input("Enter first number: ")), int(input("Enter second number: "))
print("quotient: "+str(first//second)+", remainder: "+str(first%second))



def func_sum(*a):
    total = 0
    for i in a:
        total += i
    return total

score = [73, 95, 80, 57, 99]
sumscore = func_sum(*score)
print("Total score :", sumscore)
print("Average score :", sumscore/len(score))



animals_dict = { "dog":"bow-wow", "cat":"meow-", "duck":"quack" }

def func_animals(dict):
    print(dict.get(input("Choice of dog, cat, duck, other : "), "I don't know"))

# single line declaration
# animals_dict, func_animals = ({ "dog":"bow-wow", "cat":"meow-", "duck":"quack" }, lambda dict : print(dict.get(input("Choice of dog, cat, duck, other : "), "I don't know")))

func_animals(animals_dict)
 
