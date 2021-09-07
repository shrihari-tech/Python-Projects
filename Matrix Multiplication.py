alist=[[4,5,6],
       [5,8,1],
       [7,8,3]]
blist=[[7,8,2],
       [6,1,8],
       [8,3,9]]
result=[]
for i in range(3):
    empty=[]
    for j in range(3):
        add=0
        for tot in range(3):
            add=add+alist[i][tot]*blist[tot][j]
        empty.append(add)
    blist.append(empty)
for num in blist:
    print(num)
