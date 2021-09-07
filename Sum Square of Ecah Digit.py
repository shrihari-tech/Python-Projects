#SUM OF SQUARE OF DIGITS 
num=int(input("Enter the Number to get Sum of Square of the Digits:"))
#Initilize
free=num
temp=0
#Iteretation of Loop
while num>0:
    balance = num%10
    temp=temp+balance**2
    num=num//10
#Display the Result 
print("The Sum of Square of",free,"Digits is",temp)        
        
