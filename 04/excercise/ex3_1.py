# The Triangle checker

triangleAngles = [
    int(input("1st angle: ")),
    int(input("2nd angle: ")),
    int(input("3rd angle: ")),
]

print("This is", "a valid" if (triangleAngles[0] + triangleAngles[1] + triangleAngles[2] == 180) else "an invalid", "triangle")
