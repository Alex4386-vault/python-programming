
def caesarSubstitution(sans, shift):
    wa = ""
    for i in range(len(sans)):
        if not sans[i].isalpha():
            wa += sans[i]
            continue
        wa += chr(((ord(sans[i]) - (ord('a') if sans[i].islower() else ord('A')) + shift + 26) % 26 ) + (ord('a') if sans[i].islower() else ord('A')))
    return wa
