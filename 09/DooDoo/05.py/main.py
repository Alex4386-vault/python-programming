import datetime
startDate = datetime.date.today()
print("today :", startDate)

inDate = input("end day(yyyy-mm-dd) : ")
ymd = inDate.split('-')
endDay = datetime.date(int(ymd[0]), int(ymd[1]), int(ymd[2]))

print(endDay - startDate)
