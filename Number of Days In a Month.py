#To Display the Number of Does a Month Contain
month=input("Enter a Month Name to get Number of Days:")
num=int(input("Enter Month Number:"))
#Checking Condition 
if (month=="April","June","September","November") and num%2==1:
    print(month,"Has 31 Days")
elif month=="February":
    print(month,"Has 28 Days")
else:    
    print(month,"Has 30 Days")
































