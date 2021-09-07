#ADDITION OF MATRIX
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
        addition=alist[i][j]+blist[i][j]
        empty.append(addition)
    result.append(empty)
for row in result:
    print(row)
