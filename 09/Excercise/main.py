import dateCalc
import datetime as dt

print("Today is", dt.date.today().strftime("%Y-%m-%d %a"))
print()

while True:
    cmd = input("1(date interval) 2(target date) 0(exit) : ")

    if cmd == '0':
        print("Have a good day")
        exit(0)
    elif cmd == '1':
        startDate = dateCalc.getDate("start date")
        endDate = dateCalc.getDate("end date")
        print("interval", endDate-startDate)
    elif cmd == '2':
        startDate = dateCalc.getDate("start date")
        afterDate = dt.timedelta(days=int(input("after date(ex. -10,10) : ")))
        print("target date is", (startDate + afterDate).strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print("invalid command!")
        
    print()

        