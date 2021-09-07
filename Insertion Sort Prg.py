#INSERTION SORT
listlen=int(input("Enter the List Size:"))
alist=[]
maximum=0
count=0
#Loop
while (count<listlen):
    num=int(input("Enter a Number:"))
    alist.append(num)
    count=count+1
#Displaying List
print(alist)
for i in range(listlen):
    change=i
    if alist[change]<alist[change-1]:
        (alist[change],alist[change-1])=alist[change-1],alist[change]
        change-=1
print(alist)




























                  
