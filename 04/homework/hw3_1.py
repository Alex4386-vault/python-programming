## Config
howMany = 3

for i in range(howMany):
    cost = float(input("Enter the actual cost: "))
    sales = float(input("Enter the sales amount: "))

    profitStr, lossStr, noProfitLoss = "Total Profit = {amount}",  "Total Loss Amount = {amount}", "No Profit No Loss!!!"

    print((profitStr if (sales - cost) > 0 else noProfitLoss if (sales == cost) else lossStr ).format(amount=abs(round(sales-cost,1))))
    print()
