import datetime as dt

def getDate(str):
    rawInput = input(str+" (yyyy-mm-dd) : ")
    dateParsed = rawInput.split('-')
    return dt.date(int(dateParsed[0]), int(dateParsed[1]), int(dateParsed[2]))


    