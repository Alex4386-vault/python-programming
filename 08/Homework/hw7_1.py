animals_dict = { "dog":"bow-wow", "cat":"meow-", "duck":"quack" }

def func_animals(dict):
    print(dict.get(input("Choice of dog, cat, duck, other : "), "I don't know"))

# single line declaration
# animals_dict, func_animals = ({ "dog":"bow-wow", "cat":"meow-", "duck":"quack" }, lambda dict : print(dict.get(input("Choice of dog, cat, duck, other : "), "I don't know")))

func_animals(animals_dict)
 