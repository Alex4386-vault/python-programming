import datetime

def invitationFormatGen(to, **kwargs):
    purpose = kwargs.get("purpose", "Halloween Party")
    date = kwargs.get("date", datetime.datetime(2019,10,30,12,00))
    place = kwargs.get("place", "Kangnam OO Coffee Shop")

    return "Dear "+to+", \nSubject: "+purpose+"\nDate: "+date.strftime("%Y-%m-%d %H:%M")+"\nPlace: "+place
