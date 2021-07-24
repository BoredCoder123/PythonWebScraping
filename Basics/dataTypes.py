mySet = {1, 2, 3}  # set
for i in mySet:
    print(i, end=" ")
print(" ")
mySet.add(4)
mySet.add(1)
mySet.remove(1)
for i in mySet:
    print(i, end=" ")
print(" ")

myDict = {1: 2, 2: 3}
print(myDict[1])
print(myDict.get(2, "null"))
print(myDict.get(3, "null"))
myDict[3] = 4
myDict[3] = 5
del myDict[3]
print(myDict.get(3, "null"))

myTuple = (1, 2, 3, 1)
print(myTuple)
print(myTuple[0])

myList = list("Ankit")
print(str(myList))
myList = list([1, 2, 3, 4])
print(str(myList))
for i in myList:
    print(i+1, end=" ")
print(" ")
myList.append('4')
myList.append(4)
myList.append(['4'])
myList.remove('4')
print(str(myList))
print(myList[-1])
print(myList[2:-3])
