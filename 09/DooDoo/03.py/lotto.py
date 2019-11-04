def isInBound(num):
    return 1 <= num <= 45

def addNumber(basket, num):
    if not isInBound(num):
        return False

    if num in basket:
        return False
    else:
        try:
            basket.append(num)
        except NameError:
            return False

        return True

def sortNumber(basket):
    basket.sort()

def isLottoFull(basket):
    return len(basket) >= 6

def printLotto(basket):
    if isLottoFull(basket):
        print("Lotto Number :", basket)
    else:
        print("Lotto is NOT FULL!")

if __name__ == "__main__":
    print("This is a module, you should not call me directly!")
    exit()
