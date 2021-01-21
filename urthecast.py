#written for urthecast by Krutik Soni

def main():
    oList = input("Enter original Elements: ").split()
    aList = input("Enter elements to add: ").split()
    rList = input("Enter elements to remove: ").split()
    print("\nOriginal List = %s\nAdd List = %s\nDelete List = %s\n" % (oList, aList, rList))
    newArray = immutableListFunc(oList, aList, rList)
    print("Final Array = ", newArray)

def immutableListFunc(originalList, addList, removeList):
    
    returnArray = list(dict.fromkeys(originalList + addList))
    for i in range(len(removeList)):
        returnArray.remove(removeList[i])

    returnArray = sorted(returnArray, reverse = True)
    return sorted(returnArray, key = len, reverse = True)

main()

