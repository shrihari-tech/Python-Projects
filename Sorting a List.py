#SORTING
alist=[2,4,5,67,8,9,3,1]
print(alist)
length=len(alist)
print("the Length of list is:",length)
for i in range(1,length):
    numbers=alist[i]
    print(numbers)
    change=i-1
    while change>=0:
        if numbers<alist[change]:
            alist[change+1]=alist[change]
            change=change-1
            alist[change+1]=numbers
        else:
            break
    print(alist)    
