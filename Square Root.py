#FACTORIAL OF A NUMBER BY NEWTONS METHOD
num=int(input("Enter the Square root of a Number:"))
guess=int(input("Enter the Guessing of Square Root Number:"))
#Checking Condition 
while (True):
    f_x=guess*guess-num
    f=2*guess
    root=guess-(f_x//f)
    print(root)
    guess=root
    break 
