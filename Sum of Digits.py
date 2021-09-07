#Sum of Digits
char=int(input("Enter a Sting or Number:"))
free=char
#Initilize
temp=0
#Iteration of Condition (Indefinite Loop)
while char>0:
    balance=char%10
    temp=temp+balance
    char=char//10
print("The Sum of Digits",free,"is",temp)    
