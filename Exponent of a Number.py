#Exponentiation Power of a Number
base=int(input("Enter Base of a Number:"))
exp=int(input("Enter Power of a Number:"))
temp=base
free=exp
#Iteration of Loop
while exp>1:
    temp=temp*base
    exp=exp-1
print("The base of",base,"to Power of",free,"is",temp)    
    
