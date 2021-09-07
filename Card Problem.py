#CARD PROBLEM
list_size=int(input("Enter the List Size:"))
position=0
alist=[]
while(position<list_size):
    avalue=int(input("Enter a Value:"))
    alist.append(avalue)
    position+=1
#Inserting the User Wanted Card
print(alist)
alist.append(0)
avalue=int(input("Enter a Card Number to be Inserted:"))
position=list_size-1
while(position>=0):
    if(avalue<alist[position]):
        alist[position+1]=alist[position]
    else:
        alist[position+1]=avalue
    position-=1
#Displaying all Cards Number got form User
print(alist)
    
