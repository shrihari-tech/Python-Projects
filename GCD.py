#GCD OF TWO NUMBERS
'''anum=int(input("Enter the 1st Number:"))
bnum=int(input("Enter teh 2nd Number:"))
if anum>bnum:
    small=bnum
else:
    small=anum
for i in range(1,small+1):
    if((anum%i==0) and (bnum%i==0)):
        gcd=i
return gcd
print("the gcd of",anum,"and",bnum,"is: ",end="")'''




def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number:"))

print("The H.C.F. is", compute_hcf(num1, num2))
