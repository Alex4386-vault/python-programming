bucketList = ["Seoul", "Daejeon", "Daegu", "Busan", "Jeju"]
goodPlace = ["Rome", "Paris", "Hanoi"]

# 1
print(bucketList[2:4])

# 2
print(bucketList[::2])

# 3
print(bucketList + goodPlace)

# 4
print("Paris" in goodPlace)

# 5
print(goodPlace.count("Rome"))

# 6
goodPlace.sort()
print(goodPlace)
