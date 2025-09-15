#Divisible
num = int(input("Enter number: "))
if  num%5 == 0 and num%6  == 0:
    print(f"{num} is divisible by both 5 and  6")
elif num%5 == 0:
    print(f"{num} is divisible by 5")
elif num%6 == 0:
    print(f"{num} is divisible by 6")
else:
    print(f"{num} is not divisible by 5 or 6")

    
#Count up to the  searched number
    
num =int(input("Enter number:"))
count = 1
while count <=num:
        print(count)
        count += 1
        
print("Finish!")
