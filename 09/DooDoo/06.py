import datetime

baseDate = input("baseDate (yyyy-mm-dd) : ")
baseDate = baseDate.split('-')
baseDate = datetime.date(int(baseDate[0]), int(baseDate[1]), int(baseDate[2]))

deltaDate = int(input("term (ex. -10, 10) : "))
deltaDate = datetime.timedelta(days=deltaDate)

print("Target Date is:", (baseDate+deltaDate))
