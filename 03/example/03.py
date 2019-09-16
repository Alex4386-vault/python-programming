## Formatting String

class User:
    def __init__(self, clientName, suspensionDate):
        self.clientName = clientName
        self.suspensionDate = suspensionDate
    
    def greetings(self):
        return "Good morning, {clientName} has been suspended for {suspensionDate} days.\n\nIn compliance with state and federal regulations, \nall testing candidates in the Aperture Science \nExtended Relaxation Center must be revived \nperiodically for a mandatory physical and \nmental wellness exercise.".format(clientName=self.clientName, suspensionDate=self.suspensionDate)

# Aperture Science
Chell = User("You", 50)

print(Chell.greetings())
