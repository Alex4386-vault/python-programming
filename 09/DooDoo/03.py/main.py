import lotto

basket = []

while not lotto.isLottoFull(basket):
    number = 0
    try:
        number = int(input("Enter the Number ? "))
        print(number, "===>", "Success" if lotto.addNumber(basket, number) else "Fail", basket, end='')
        print()
    except ValueError:
        print("Invalid Number! Try again!")

print()
lotto.sortNumber(basket)
lotto.printLotto(basket)
