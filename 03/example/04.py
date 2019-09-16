## Formatting String

class User:
    def __init__(self, clientName, suspensionDate):
        self.clientName = clientName
        self.suspensionDate = suspensionDate
    
    def greetings(self):
        suspensionDate = self.suspensionDate
        return "Good morning, {0} has been suspended for %d days".format(self.clientName) % suspensionDate

# Aperture Science
Chell = User("You", 50)

print(Chell.greetings())