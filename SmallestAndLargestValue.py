largest = None
smallest = None

while True:
    num = input("Enter a Number: ")
    if num == "done": break
    
    try :
        n = int(num)
    except:
        print("Not a Number")
        continue
    else:
        if (largest is None):
            largest = n
        elif (largest < n):
            largest = n
        if (smallest is None):
            smallest = n
        elif (smallest > n):
            smallest = n

print("Smallest is ", smallest)
print("Largest is ", largest)
