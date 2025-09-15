'''myList =[]
myList = ["Ladesma" , "Guyo" , "Diocares" , "Dela Cruz"]
myList.append("Bangcaya")
lista = ["Damian", "Fragata"]
myList.append(lista)
myList.insert(1, "John")

print(myList)
print(myList[2])
print(myList[:  : -1])
print(myList[1:3:2])
myList.pop(0)
myList.remove("Guyo")
list2 = ["Bangcaya" , "Calip"]

print(myList + list2)
myList.sort()
myList.reverse()
print(myList)

print ("range")
for x in myList:
    print(f"{x}" , end =" ")
    
for y in range(len(myList)):
    print(f"{myList[y]}", end = " ") '''
    
#apend - dagdag
'''    
myList2= []
for x in range(3):
    print("Enter Number: ")
    num1 = float(input())
    myList2.append(num1)
print(myList2)

nestedList = [[12,5, 3], [6,9, 5]]
print (nestedList[1][0])

for x in range (len(nestedList)):
    for y in range (len(nestedList[y])):
        print(f"{nestedList[x][y]}", end =" ")
        
    print()
'''
'''
scores = []

row = int(input("Enter rows: "))
col = int(input("Enter columns: "))

for i in range(1, row + 1):
    print(f"\nRow {i}")
    for j in range(1, col + 1):
        score = int(input(f"   Enter row {i} score{j}: "))
        scores.append(score)

total = sum(scores)
average = total / len(scores)

print("\nScores:", scores)
print("Sum =", total)
print("Average =", average)


'''
'''
myTuple = (1,4,5,6)
x=list(myTuple)
x.append(8)
x.append(70)
x.remove(5)
x.pop()

myTuple2 = tuple(x)
print(myTuple2)

for x in myTuple2:
    print(x, end ="  ")
    
'''
    
myDict = {"id" : "URDA-011"
          "name: " "Ladesma",
          "salary": 10000.00 }
myDict["age"] = 28
print(myDict)
myDict["sex"] = "female"
myDict["name"] = "Archilyn"
myDict.popitem()
myDict.pop("name")
print(myDict)

                 
    
 


