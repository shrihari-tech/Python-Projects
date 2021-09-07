num= int(input("Enter a Number:"))
for aNum in range(2,num):
    ini = 0
    for divisor in range(1,aNum+1):
        if aNum % divisor ==0:
            ini+=1
    if ini == 2:
            print("The Prime Numbers Between",num,"is",aNum)
