class MissingNoError(Exception):
    pass

class Animal:
    name = None
    sound = None
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def bark(self):
        if self.name is None or self.sound is None:
            print("MISSINGNO. sounds h̶̖̥̳͈̳̮͔͚̭̟͉͆̎̀̒̏̈́̔͐̈́̚̕͝d̴̞̥͎̑͐̉̓̒̍̆̓̈́̀͝ķ̶̙͉̲̦̙͕͖͖̩̝̩̯̣̆̅̇̅̐̆̚g̶͎͑̓̇̅̇̈́̽̎̿͗̋̕ñ̵̡̝̮͓̫̱̙̹͉̳͎̀͜d̸̨̰͍͕͎̪̰̼̜͑͐̍̈́̈́͐̄̉̈̔͝ͅj̷̪͆̏̈́̃̎̅̇̌̅̾͊̇͝k̵̢͙̦̪̗̣̳̰͕̩̮̰͊͐͒̂̇͠͝ͅl̸̤̙̮͎͉̗̹̯̟͎̙̇̓͌̄̃͑̆͆̓̓͌͌̎͝ḋ̸͔s̶̬̞͈̣͉̫̗̖̿͋͆̏̈́f̶̡̨̛͚̱͚̞͍͓̜̥̀͑͑̄̒")
            raise MissingNoError("YOU ARE FUCKED")
        else:
            print(self.name,"sounds",self.sound)

dog = Animal("dog", "bow-wow")
dog.bark()

cat = Animal("cat", "meow")
cat.bark()

missingno = Animal(None, None)
missingno.bark()
