#PALINDROME
num=int(input("Enter a String:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print("Its a Palindrome")
else:
    print("Its Not a Palindrome")
