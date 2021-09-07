#FACTORIAL OF A NUMBER
num=int(input("Enter a Number to Get its Factorial:"))
storage=1
for avalue in range(1,num+1):
    storage=storage*avalue
print("Factorial of",num,"is",storage)    
