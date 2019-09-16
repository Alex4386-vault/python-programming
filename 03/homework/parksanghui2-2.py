try:
    mrFahrenheit = float(input("Please enter a temperature in ℉ : "))
except ValueError:
    print("Improper input detected")
    exit(1)

print("{mrFahrenheit} ℉ = {superSonicManOuttaYou} ℃".format(mrFahrenheit = mrFahrenheit, superSonicManOuttaYou = (5/9) * (mrFahrenheit - 32)))
