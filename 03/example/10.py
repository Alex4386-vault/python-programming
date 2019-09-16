
def sec2MinSec(sec):
    minute = sec // 60
    second = sec % 60
    return minute,second

def getIntInput(ah):
    validNumbers = False

    while not validNumbers:
        try:
            No = int(input(ah))
        except ValueError:
            print("Enter Valid Number!!")
        else:
            validNumbers = True
            return No

sec = getIntInput("Enter seconds: ")

minute, sec = sec2MinSec(sec)
print(str(minute)+":"+str(sec).zfill(2))
