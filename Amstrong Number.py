#Amstrong Number
num= int(input("Enter a Amstrong number [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748] : "))
sum = 0
temp=num
#Iteration of Loop
while temp>0:
   digit=temp%10
   sum=sum+digit**3
   temp=temp//10
#Checking of Condition that User Ented is Equal to Amstrong Number   
if num == sum:
   print("The Given Number",num,"is an Armstrong number")
else:
   print("The Given Number",num,"is not an Armstrong number")
