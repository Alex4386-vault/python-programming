bucketList = ["Seoul", "Daegu", "Busan"]

bucketList.append("Jeju")
print(bucketList)

print(len(bucketList))

bucketList.insert(1, "Daejeon")
print(bucketList)

bucketList.remove("Seoul")
print(bucketList)

# del bucketList[len(bucketList) - 1]
# or
bucketList.pop()
print(bucketList)

bucketList.clear()
print(bucketList)
